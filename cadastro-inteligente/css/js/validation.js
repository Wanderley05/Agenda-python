// Elementos do formulário
const nome = document.getElementById("nome");
const email = document.getElementById("email");
const senha = document.getElementById("senha");
const confirmar = document.getElementById("confirmar");

// Elementos de força de senha
const strengthFill = document.getElementById("strength-fill");
const strengthText = document.getElementById("strength-text");

// Elementos do form
const form = document.getElementById("cadastroForm");
const botao = document.querySelector("button");
const mensagemFinal = document.getElementById("mensagem-final");

// Verificar se todos os elementos existem
const elementosObrigatorios = [nome, email, senha, confirmar, form, botao, mensagemFinal];
if (elementosObrigatorios.some(el => !el)) {
  console.error("Erro: Alguns elementos do formulário estão faltando no HTML");
}

nome.addEventListener("blur", () => validarCampo(nome, validarNome));
email.addEventListener("blur", () => validarCampo(email, validarEmail));
senha.addEventListener("input", () => {
  validarCampo(senha, validarSenha);
  verificarForcaSenha(senha.value);
});
confirmar.addEventListener("blur", () => validarCampo(confirmar, validarConfirmar));

function validarCampo(input, funcao) {
  const msg = document.getElementById(input.id + "-error");
  const resultado = funcao(input.value);

  if (!resultado.valido) {
    input.classList.add("error");
    input.classList.remove("success");

    msg.textContent = "Inválido ❌ - " + resultado.mensagem;
    msg.classList.add("error");
    msg.classList.remove("success");

  } else {
    input.classList.remove("error");
    input.classList.add("success");

    msg.textContent = "Válido ✔️";
    msg.classList.add("success");
    msg.classList.remove("error");
  }
}

function validarNome(valor) {
  if (!valor.trim()) return { valido: false, mensagem: "Nome obrigatório" };
  if (valor.length < 3) return { valido: false, mensagem: "Mínimo 3 caracteres" };
  return { valido: true };
}

function validarEmail(valor) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  if (!valor) return { valido: false, mensagem: "Email obrigatório" };
  if (valor.length < 5) return { valido: false, mensagem: "Email muito curto" };
  if (!regex.test(valor)) return { valido: false, mensagem: "Formato inválido" };
  return { valido: true };
}

function validarSenha(valor) {
  if (valor.length < 8) return { valido: false, mensagem: "Mínimo 8 caracteres" };
  if (!/[A-Z]/.test(valor)) return { valido: false, mensagem: "Precisa de letra maiúscula" };
  if (!/[0-9]/.test(valor)) return { valido: false, mensagem: "Precisa de número" };
  return { valido: true };
}

function validarConfirmar(valor) {
  if (valor !== senha.value) {
    return { valido: false, mensagem: "Senhas não coincidem" };
  }
  return { valido: true };
}

function verificarForcaSenha(valor) {
  let pontos = 0;

  if (valor.length >= 8) pontos++;
  if (/[A-Z]/.test(valor)) pontos++;
  if (/[0-9]/.test(valor)) pontos++;
  if (/[^A-Za-z0-9]/.test(valor)) pontos++;

  strengthFill.className = "";
  strengthFill.style.width = "0%";

  if (valor.length === 0) {
    strengthText.textContent = "";
  } else if (pontos === 1) {
    strengthFill.classList.add("fraca");
    strengthFill.style.width = "25%";
    strengthText.textContent = "Senha fraca";
  } else if (pontos === 2) {
    strengthFill.classList.add("razoavel");
    strengthFill.style.width = "50%";
    strengthText.textContent = "Senha razoável";
  } else if (pontos === 3) {
    strengthFill.classList.add("boa");
    strengthFill.style.width = "75%";
    strengthText.textContent = "Senha boa";
  } else if (pontos === 4) {
    strengthFill.classList.add("forte");
    strengthFill.style.width = "100%";
    strengthText.textContent = "Senha forte";
  }
}

form.addEventListener("submit", function(e) {
  e.preventDefault();

  const validacoes = [
    validarNome(nome.value),
    validarEmail(email.value),
    validarSenha(senha.value),
    validarConfirmar(confirmar.value)
  ];

  const tudoValido = validacoes.every(v => v.valido);

  if (!tudoValido) {
    mensagemFinal.style.color = "red";
    mensagemFinal.textContent = "❌ Corrija os campos antes de enviar";
    return;
  }

  botao.disabled = true;
  botao.innerHTML = 'Enviando... <span class="spinner"></span>';

  setTimeout(() => {
    mensagemFinal.style.color = "green";
    mensagemFinal.textContent = "✅ Cadastro realizado com sucesso!";

    form.reset();

    document.querySelectorAll("input").forEach(i => {
      i.classList.remove("success", "error");
    });

    document.querySelectorAll(".msg").forEach(m => m.textContent = "");

    strengthFill.className = "";
    strengthFill.style.width = "0%";
    strengthText.textContent = "";

    botao.disabled = false;
    botao.textContent = "Cadastrar";

  }, 2000);
});