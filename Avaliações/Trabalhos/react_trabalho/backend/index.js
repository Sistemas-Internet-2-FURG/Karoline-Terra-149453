const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;
const mysql = require('mysql');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

app.use(cors());
app.use(express.json());

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'cute_tasks',
});

connection.connect((err) => {
  if (err) {
    console.error('Error connecting: ' + err.stack);
    return;
  }
  console.log('Connected as id ' + connection.threadId);
});

app.post('/register', (req, res) => {
  const { username, email, password } = req.body;

  const checkUserQuery = 'SELECT * FROM users WHERE email = ?';
  connection.query(checkUserQuery, [email], (err, results) => {
    if (results.length > 0) {
      return res.status(400).send('Usuário já registrado');
    }

    const hashedPassword = bcrypt.hashSync(password, 8);

    const insertUserQuery =
      'INSERT INTO users (username, email, password) VALUES (?, ?, ?)';
    connection.query(
      insertUserQuery,
      [username, email, hashedPassword],
      (err, result) => {
        if (err) {
          console.error('Erro ao registrar usuário:', err);
          return res.status(500).send('Erro ao registrar usuário');
        }
        const token = jwt.sign({ id: result.insertId }, 'secreta', {
          expiresIn: '1h',
        });
        res.status(201).json({ auth: true, token });
      },
    );
  });
});

app.post('/login', (req, res) => {
  const { email, password } = req.body;

  const query = 'SELECT * FROM users WHERE email = ?';
  connection.query(query, [email], (err, results) => {
    if (err) {
      console.error('Erro ao buscar usuário:', err);
      return res.status(500).send('Erro ao buscar usuário');
    }

    if (results.length === 0) {
      return res.status(404).send('Usuário não encontrado');
    }
    const user = results[0];

    const passwordIsValid = bcrypt.compareSync(password, user.password);
    if (!passwordIsValid) {
      return res.status(401).send({ auth: false, token: null });
    }

    const token = jwt.sign({ id: user.id }, 'secreta', { expiresIn: '1h' });
    res.status(200).json({ auth: true, token });
  });
});

const verifyToken = (req, res, next) => {
  const token = req.headers['x-access-token'];
  if (!token) {
    return res.status(403).send({ auth: false, message: 'Nenhum token fornecido.' });
  }

  jwt.verify(token, 'secreta', (err, decoded) => {
    if (err) {
      return res.status(500).send({ auth: false, message: 'Falha na autenticação do token.' });
    }

    req.userId = decoded.id;
    next();
  });
};

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

app.get('/tasks', verifyToken, (req, res) => {
  const query = 'SELECT * FROM tasks WHERE user_id = ?';
  connection.query(query, [req.userId], (err, results) => {
    if (err) {
      console.error('Erro ao buscar tarefas:', err);
      return res.status(500).send('Erro ao buscar tarefas');
    }

    res.json(results);
  });
});

app.post('/tasks', verifyToken, (req, res) => {
  const { name, description, status } = req.body;
  const query = 'INSERT INTO tasks (user_id, name, description, status) VALUES (?, ?, ?, ?)';

  connection.query(query, [req.userId, name, description, status], (err, result) => {
    if (err) {
      console.error('Erro ao adicionar tarefa:', err);
      return res.status(500).send('Erro ao adicionar tarefa');
    }

    res.status(201).json({ id: result.insertId, user_id: req.userId, name, description, status });
  });
});


app.delete('/tasks/:id', (req, res) => {
  const taskId = req.params.id;

  const query = 'DELETE FROM tasks WHERE id = ?';

  connection.query(query, [taskId], (err, result) => {
    if (err) {
      console.error('Erro ao deletar tarefa:', err);
      res.status(500).send('Erro ao deletar tarefa');
    } else {
      if (result.affectedRows === 0) {
        res.status(404).send('Tarefa não encontrada');
      } else {
        res.status(200).send('Tarefa deletada com sucesso');
      }
    }
  });
});

app.put('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  const { status } = req.body;

  const validStatuses = ['A fazer', 'Em andamento', 'Concluída'];
  if (!validStatuses.includes(status)) {
    return res.status(400).send('Status inválido');
  }

  const query = 'UPDATE tasks SET status = ? WHERE id = ?';

  connection.query(query, [status, taskId], (err, result) => {
    if (err) {
      console.error('Erro ao atualizar o status da tarefa:', err);
      res.status(500).send('Erro ao atualizar o status da tarefa');
    } else {
      if (result.affectedRows === 0) {
        res.status(404).send('Tarefa não encontrada');
      } else {
        res.status(200).send('Status da tarefa atualizado com sucesso');
      }
    }
  });
});
