
-- \c fastapi_db  gente é o nome para conectar com BD

-- Criação da tabela de perguntas
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela de respostas
CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

