<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crie seu Currículo</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Crie seu Currículo</h1>
        <form id="resumeForm">
            <div class="form-group">
                <label for="name">Nome Completo:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Telefone:</label>
                <input type="text" id="phone" name="phone" required>
            </div>
            <div class="form-group">
                <label for="linkedin">LinkedIn:</label>
                <input type="text" id="linkedin" name="linkedin">
            </div>
            <div class="form-group">
                <label for="github">GitHub:</label>
                <input type="text" id="github" name="github">
            </div>
            <div class="form-group">
                <label for="professional_summary">Resumo Profissional:</label>
                <textarea id="professional_summary" name="professional_summary"></textarea>
            </div>
            <div class="form-group">
                <label for="professional_experience">Experiência Profissional:</label>
                <textarea id="professional_experience" name="professional_experience"></textarea>
            </div>
            <div class="form-group">
                <label for="education">Formação Acadêmica:</label>
                <textarea id="education" name="education"></textarea>
            </div>
            <div class="form-group">
                <label for="certifications">Certificações:</label>
                <textarea id="certifications" name="certifications"></textarea>
            </div>
            <div class="form-group">
                <label for="technologies">Tecnologias Utilizadas:</label>
                <textarea id="technologies" name="technologies"></textarea>
            </div>
            <div class="form-group">
                <label for="methodologies">Metodologias:</label>
                <textarea id="methodologies" name="methodologies"></textarea>
            </div>
            <div class="form-group">
                <label for="tools">Ferramentas:</label>
                <textarea id="tools" name="tools"></textarea>
            </div>
            <div class="form-group">
                <label for="others">Outros:</label>
                <textarea id="others" name="others"></textarea>
            </div>
            <div class="form-group">
                <label for="languages">Idiomas:</label>
                <textarea id="languages" name="languages"></textarea>
            </div>
            <div class="form-group">
                <label for="operating_systems">Sistemas Operacionais:</label>
                <textarea id="operating_systems" name="operating_systems"></textarea>
            </div>
            <button type="submit">Gerar Currículo</button>
        </form>
    </div>
    <script src="app.js"></script>
</body>
</html>
