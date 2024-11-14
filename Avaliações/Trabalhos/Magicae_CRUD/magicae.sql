-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05/09/2024 às 02:24
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `magicae`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

CREATE TABLE `alunos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `data_nascimento` date NOT NULL,
  `feitico_favorito_id` int(11) DEFAULT NULL,
  `patrono` varchar(255) DEFAULT NULL,
  `casa_id` int(11) DEFAULT NULL,
  `disciplina_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `alunos`
--

INSERT INTO `alunos` (`id`, `nome`, `data_nascimento`, `feitico_favorito_id`, `patrono`, `casa_id`, `disciplina_id`) VALUES
(1, 'Harry Potter', '1980-07-31', 4, 'Cervo', 1, 2),
(2, 'Hermione Granger', '1979-09-19', 2, 'Castor', 1, 1),
(3, 'Ron Weasley', '1980-03-01', 1, 'Cachorro', 1, 3),
(4, 'Draco Malfoy', '1980-06-05', 10, 'Serpente', 2, 2),
(5, 'Luna Lovegood', '1981-02-13', 5, 'Lebre', 3, 6),
(7, 'Valdira', '2001-07-08', 1, 'Fenix', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `casas`
--

CREATE TABLE `casas` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `simbolo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `casas`
--

INSERT INTO `casas` (`id`, `nome`, `simbolo`) VALUES
(1, 'Grifinória', 'Leão'),
(2, 'Sonserina', 'Serpente'),
(3, 'Corvinal', 'Águia'),
(4, 'Lufa-Lufa', 'Texugo');

-- --------------------------------------------------------

--
-- Estrutura para tabela `criaturas_magicas`
--

CREATE TABLE `criaturas_magicas` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `local_origem` varchar(255) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `criaturas_magicas`
--

INSERT INTO `criaturas_magicas` (`id`, `nome`, `local_origem`, `descricao`) VALUES
(1, 'Dragão', 'Diversos locais mágicos', 'Criatura imponente e poderosa, conhecida por seu fogo mortal e escamas resistentes. Existem várias espécies, como o Dragão Húngaro e o Dragão Chinês.'),
(2, 'Hipogrifo', 'Floresta de Hogwarts', 'Criatura mágica com a parte dianteira de uma águia e a parte traseira de um cavalo. É conhecida por sua força e lealdade, mas pode ser perigosa se não for respeitada.'),
(3, 'Centauro', 'Floresta Proibida', 'Seres mágicos com o corpo de um cavalo e a parte superior de um homem. São conhecidos por sua sabedoria e habilidades com o arco e flecha.'),
(4, 'Fênix', 'Diversos locais mágicos', 'Ave mágica que renasce das próprias cinzas. Tem penas de ouro e vermelho e seu canto possui propriedades curativas. É um símbolo de renascimento e imortalidade.'),
(5, 'Basilisco', 'Câmara Secreta', 'Serpente gigante e venenosa com um olhar mortal. Conhecida por seu veneno poderoso e por petrificar qualquer criatura que o olhe diretamente nos olhos.'),
(6, 'Niffler', 'Diversos locais mágicos', 'Pequena criatura peluda que é atraída por objetos brilhantes e valiosos. Conhecida por sua habilidade de armazenar itens em uma bolsa mágica.'),
(7, 'Sereia', 'Lago de Hogwarts', 'Criatura aquática com a parte superior de uma mulher e a parte inferior de um peixe. Conhecida por seu canto encantador e suas habilidades de nadar rapidamente.'),
(8, 'Testrálio', 'Floresta Proibida', 'Cavalo alado esquelético visível apenas para aqueles que já viram a morte. É uma criatura rara e geralmente é associada com a morte e o luto.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas`
--

CREATE TABLE `disciplinas` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `disciplinas`
--

INSERT INTO `disciplinas` (`id`, `nome`, `descricao`) VALUES
(1, 'Transfiguração', 'A disciplina que ensina a transformar um objeto em outro, utilizando feitiços e encantamentos.'),
(2, 'Defesa Contra as Artes das Trevas', 'Curso focado em ensinar técnicas de defesa contra feitiços das trevas e criaturas malignas.'),
(3, 'Poções', 'Ensina a preparar poções mágicas e seus efeitos, bem como o manuseio de ingredientes mágicos.'),
(5, 'Herbologia', 'Estudo das plantas mágicas e suas propriedades, incluindo cultivo e uso de ervas e fungos.'),
(6, 'Astronomia', 'Curso sobre o estudo das estrelas e corpos celestes, suas influências e fenômenos astronômicos.'),
(7, 'História da Magia', 'Disciplina que cobre a história do mundo bruxo, incluindo eventos significativos e figuras importantes.'),
(8, 'Estudos dos Trouxas', 'Estudo da vida dos trouxas e suas culturas, abordando a interação com o mundo mágico.'),
(9, 'Feitiçaria', 'Estudo avançado de feitiços e encantamentos'),
(10, 'Adivinhação', 'A arte de prever o futuro e interpretar sinais.'),
(11, 'Trato das Criaturas Mágicas', 'Estudo sobre criaturas mágicas e seu cuidado.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `feiticos`
--

CREATE TABLE `feiticos` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `feiticos`
--

INSERT INTO `feiticos` (`id`, `nome`, `descricao`) VALUES
(1, 'Expelliarmus', 'Feitiço de desarmamento. Usado para desarmar um oponente, removendo qualquer objeto que ele esteja segurando.'),
(2, 'Lumos', 'Feitiço de iluminação. Produz uma luz na ponta da varinha do bruxo, funcionando como uma lanterna.'),
(3, 'Wingardium Leviosa', 'Feitiço de levitação. Permite que objetos sejam levantados e movidos no ar.'),
(4, 'Expecto Patronum', 'Feitiço do Patrono. Cria um Patrono, uma entidade mágica que afugenta Dementadores e Lethifolds.'),
(5, 'Accio', 'Feitiço convocatório. Atrai objetos para o bruxo que o conjura, mesmo a longa distância.'),
(6, 'Stupefy', 'Feitiço de atordoamento. Atordoa o alvo, deixando-o inconsciente por um curto período de tempo.'),
(7, 'Alohomora', 'Feitiço de desbloqueio. Usado para destrancar portas e janelas trancadas.'),
(8, 'Obliviate', 'Feitiço de memória. Apaga ou altera as memórias de uma pessoa.'),
(9, 'Transformação', 'Feitiço usado para transformar um objeto em outro.'),
(10, 'Sectumsempra', 'Feitiço que causa cortes profundos e sangramentos no alvo.'),
(11, 'Herbivicus', 'Feitiço usado para acelerar o crescimento das plantas.'),
(12, 'Divination', 'Feitiço relacionado arte da adivinhação.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros`
--

CREATE TABLE `livros` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `data_publicacao` date NOT NULL,
  `descricao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `livros`
--

INSERT INTO `livros` (`id`, `nome`, `data_publicacao`, `descricao`) VALUES
(1, 'Hogwarts: Uma História', '1991-07-31', 'Um livro famoso na comunidade bruxa que narra a história da Escola de Magia e Bruxaria de Hogwarts, seus fundadores e seus eventos mais importantes.'),
(2, 'O Livro Monstruoso dos Monstros', '1993-08-02', 'Um livro de estudo usado na disciplina de Trato das Criaturas Mágicas. O livro é conhecido por seu comportamento agressivo e é difícil de ser manuseado.'),
(3, 'As Aventuras de Martin Miggs, o Trouxa', '1982-05-10', 'Um livro de quadrinhos populares no mundo bruxo que narra as histórias de um trouxa chamado Martin Miggs e suas confusões.'),
(4, 'Os Contos de Beedle, o Bardo', '1400-08-01', 'Uma coleção de contos de fadas populares entre os jovens bruxos. Um dos contos mais famosos é \"O Conto dos Três Irmãos\".'),
(5, 'Quadribol Através dos Séculos', '1952-10-03', 'Um guia sobre a história do Quadribol, o esporte mais popular entre os bruxos, detalhando suas regras e sua evolução ao longo dos séculos.'),
(6, 'As Forças das Trevas: Um Guia de Autoproteção', '1992-09-01', 'Um livro sobre como se proteger contra as forças das trevas, incluindo defesa contra feitiços malignos e criaturas perigosas.'),
(7, 'Poções Avançadas', '1985-09-12', 'Um livro de referência para estudantes avançados em poções, contendo receitas e instruções para preparar poções complexas e poderosas.');

-- --------------------------------------------------------

--
-- Estrutura para tabela `professores`
--

CREATE TABLE `professores` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `data_nascimento` date NOT NULL,
  `casa_id` int(11) DEFAULT NULL,
  `feitico_favorito_id` int(11) DEFAULT NULL,
  `disciplina_id` int(11) DEFAULT NULL,
  `patrono` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `professores`
--

INSERT INTO `professores` (`id`, `nome`, `data_nascimento`, `casa_id`, `feitico_favorito_id`, `disciplina_id`, `patrono`) VALUES
(1, 'Minerva McGonagall', '1935-10-04', 1, 9, 1, 'Gato'),
(2, 'Severus Snape', '1960-01-09', 2, 10, 3, 'Serpente'),
(3, 'Filius Flitwick', '1960-10-17', 3, 3, 9, 'Pipistrello'),
(4, 'Pomona Sprout', '1950-05-15', 4, 11, 5, 'Texugo'),
(5, 'Sybill Trelawney', '1964-03-09', 3, 12, 10, 'Águia'),
(6, 'Rubeus Hagrid', '1928-12-06', 1, 7, 11, 'Dragão');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_type` enum('professor','aluno') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `user_type`) VALUES
(1, 'Karol', 'pbkdf2:sha256:600000$ntrtduM7$94165df892431b7aefea2e6ccd9e668b7b3e5a80bb66b52105c690dff852389f', 'professor'),
(2, 'Luna', 'pbkdf2:sha256:600000$JrAG2SHG$d66fd8c6b20ae4fa2e1fb8c540cdbf3c9344ff3cf0bfaeac8ee67bfb5a81bc5e', 'aluno');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `feitico_favorito_id` (`feitico_favorito_id`),
  ADD KEY `casa_id` (`casa_id`),
  ADD KEY `disciplina_id` (`disciplina_id`);

--
-- Índices de tabela `casas`
--
ALTER TABLE `casas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `criaturas_magicas`
--
ALTER TABLE `criaturas_magicas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `feiticos`
--
ALTER TABLE `feiticos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `livros`
--
ALTER TABLE `livros`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `professores`
--
ALTER TABLE `professores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `casa_id` (`casa_id`),
  ADD KEY `feitico_favorito_id` (`feitico_favorito_id`),
  ADD KEY `disciplina_id` (`disciplina_id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `casas`
--
ALTER TABLE `casas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `criaturas_magicas`
--
ALTER TABLE `criaturas_magicas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de tabela `feiticos`
--
ALTER TABLE `feiticos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de tabela `livros`
--
ALTER TABLE `livros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `professores`
--
ALTER TABLE `professores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `alunos`
--
ALTER TABLE `alunos`
  ADD CONSTRAINT `alunos_ibfk_1` FOREIGN KEY (`feitico_favorito_id`) REFERENCES `feiticos` (`id`),
  ADD CONSTRAINT `alunos_ibfk_2` FOREIGN KEY (`casa_id`) REFERENCES `casas` (`id`),
  ADD CONSTRAINT `alunos_ibfk_3` FOREIGN KEY (`disciplina_id`) REFERENCES `disciplinas` (`id`);

--
-- Restrições para tabelas `professores`
--
ALTER TABLE `professores`
  ADD CONSTRAINT `professores_ibfk_1` FOREIGN KEY (`casa_id`) REFERENCES `casas` (`id`),
  ADD CONSTRAINT `professores_ibfk_2` FOREIGN KEY (`feitico_favorito_id`) REFERENCES `feiticos` (`id`),
  ADD CONSTRAINT `professores_ibfk_3` FOREIGN KEY (`disciplina_id`) REFERENCES `disciplinas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
