const questionsVf = [
  {
    pregunta: "L'hidrogen és un metall alcalí.",
    respostaCorrecta: false,
    tipus: "Propietats",
  },
  {
    pregunta: "L'oxigen és l'element més abundant a l'escorça terrestre.",
    respostaCorrecta: true,
    tipus: "Abundància",
  },
  {
    pregunta: "La plata té el símbol químic 'Ag'.",
    respostaCorrecta: true,
    tipus: "Símbols",
  },
  {
    pregunta: "Tots els gasos nobles són radioactius.",
    respostaCorrecta: false,
    tipus: "Propietats",
  },
  {
    pregunta: "L'or és un excel·lent conductor de l'electricitat.",
    respostaCorrecta: true,
    tipus: "Propietats",
  },
  {
    pregunta: "El mercuri és l'únic metall líquid a temperatura ambient.",
    respostaCorrecta: true,
    tipus: "Propietats",
  },
  {
    pregunta: "El Carboni (C) és l'element base de la vida orgànica.",
    respostaCorrecta: true,
    tipus: "Composició",
  },
  {
    pregunta: "La taula periòdica actual ordena els elements per massa atòmica.",
    respostaCorrecta: false, // S'ordena per número atòmic
    tipus: "Història",
  },
  {
    pregunta: "El clor és un gas noble.",
    respostaCorrecta: false, // El clor és un halògen
    tipus: "Grups",
  },
  {
    pregunta: "El ferro és un element essencial per a l'hemoglobina en la sang.",
    respostaCorrecta: true,
    tipus: "Biologia",
  },
  {
    pregunta: "El diamant i el grafit estan fets del mateix element químic.",
    respostaCorrecta: true, // Tots dos són formes al·lotròpiques del carboni
    tipus: "Composició",
  },
  {
    pregunta: "L'heli és més pesat que l'aire.",
    respostaCorrecta: false,
    tipus: "Propietats",
  },
  {
    pregunta: "El sodi reacciona violentament amb l'aigua.",
    respostaCorrecta: true,
    tipus: "Reaccions",
  },
  {
    pregunta: "El neó s'utilitza habitualment en anuncis lluminosos.",
    respostaCorrecta: true,
    tipus: "Aplicacions",
  },
  {
    pregunta: "El plom té el símbol químic 'Pb'.",
    respostaCorrecta: true,
    tipus: "Símbols",
  },
  {
    pregunta: "L'ozó és una molècula de tres àtoms d'oxigen.",
    respostaCorrecta: true,
    tipus: "Composició",
  },
  {
    pregunta: "El calci és el metall més abundant a l'escorça terrestre.",
    respostaCorrecta: false, // És l'alumini
    tipus: "Abundància",
  },
  {
    pregunta: "Tots els metalls condueixen bé la calor i l'electricitat.",
    respostaCorrecta: true,
    tipus: "Propietats",
  },
  {
    pregunta: "Els elements del grup 18 es coneixen com a halògens.",
    respostaCorrecta: false, // Són els gasos nobles
    tipus: "Grups",
  },
  {
    pregunta: "El fluor és l'element més electronegatiu.",
    respostaCorrecta: true,
    tipus: "Propietats",
  },
];

let scoreVf = 0;
let totalQuestionsVf = 10;
let questionsAskedVf = 0;
let timerIntervalVf = null;
let questionsPoolVf = [];

// Variables per a la comunicació amb el servidor (si es manté la funcionalitat)
let game_id_vf = 0;
let seed_vf = 0;
let intervalStatusVf = null;

const formulariVf = document.getElementById("formulari-vf");
const jocVf = document.getElementById("joc-vf");
const resultatVf = document.getElementById("resultat-vf");
const cronoVf = document.getElementById("crono-vf");
const scoreDisplayVf = document.getElementById("score-vf");
const progressDisplayVf = document.getElementById("progress-vf");
const questionDisplayVf = document.getElementById("question-vf");
const optionsDivVf = document.getElementById("options-vf");
const feedbackVf = document.getElementById("feedback-vf");
const missatgeFinalVf = document.getElementById("missatgeFinalVf");

const tornarMenuJocVfBtn = document.getElementById("tornarMenuJocVf");
const tornarMenuResultatVfBtn = document.getElementById("tornarMenuResultatVf");

function shuffleArray(array) {
  // Use a simple random shuffle if seed is not critical for local game
  return array
    .map((value) => ({ value, sort: Math.random() })) // Changed from seed to Math.random() for local shuffle
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
}

function startTimerVf(duration) {
  clearInterval(timerIntervalVf);
  let timeLeft = duration;
  cronoVf.textContent = `Temps restant: ${timeLeft}s`;

  timerIntervalVf = setInterval(() => {
    timeLeft--;
    cronoVf.textContent = `Temps restant: ${timeLeft}s`;
    if (timeLeft <= 0) {
      clearInterval(timerIntervalVf);
      feedbackVf.textContent = "Temps esgotat!";
      feedbackVf.classList.remove('correct-text', 'error-text');
      feedbackVf.classList.add('error-text');
      disableOptionsVf();
      setTimeout(nextQuestionOrEndVf, 1500);
    }
  }, 1000);
}

function disableOptionsVf() {
  const buttons = optionsDivVf.querySelectorAll("button");
  buttons.forEach((btn) => {
    btn.disabled = true;
  });
}

function enableOptionsVf() {
  const buttons = optionsDivVf.querySelectorAll("button");
  buttons.forEach((btn) => {
    btn.disabled = false;
  });
}

function getNewQuestionVf() {
  // Neteja les classes de feedback i colors de les opcions anteriors
  feedbackVf.textContent = "";
  feedbackVf.classList.remove('correct-text', 'error-text');

  const optionButtons = optionsDivVf.querySelectorAll(".option-vf");
  optionButtons.forEach(btn => {
      btn.classList.remove('correct', 'incorrect');
      btn.disabled = false; // Re-habilita els botons
  });


  if (questionsAskedVf >= totalQuestionsVf) {
    acabarJocVf();
    return;
  }

  const current = questionsPoolVf[questionsAskedVf];

  questionsAskedVf++;

  progressDisplayVf.textContent = `Pregunta ${questionsAskedVf} de ${totalQuestionsVf}`;
  questionDisplayVf.textContent = current.pregunta;

  // Assegura't que els botons True/False estiguin sempre presents i actius
  // No cal recrear l'HTML si ja està en el DOM, només actualitzar-lo
  const trueBtn = optionsDivVf.querySelector(".true-button");
  const falseBtn = optionsDivVf.querySelector(".false-button");

  trueBtn.onclick = () => checkAnswerVf(true, current.respostaCorrecta, trueBtn);
  falseBtn.onclick = () => checkAnswerVf(false, current.respostaCorrecta, falseBtn);

  startTimerVf(15);
}

function checkAnswerVf(selected, correct, clickedButton) {
  clearInterval(timerIntervalVf);
  disableOptionsVf();

  const trueBtn = optionsDivVf.querySelector(".true-button");
  const falseBtn = optionsDivVf.querySelector(".false-button");

  // Marca la resposta correcta en verd
  if (correct === true) {
      trueBtn.classList.add('correct');
      falseBtn.classList.add('incorrect'); // Si la correcta es VERITAT, FALS es incorrecta
  } else { // correct === false
      falseBtn.classList.add('correct');
      trueBtn.classList.add('incorrect'); // Si la correcta es FALS, VERITAT es incorrecta
  }

  // Si l'usuari ha seleccionat la incorrecta, la marca explícitament
  if (selected !== correct) {
      clickedButton.classList.add('incorrect');
      clickedButton.classList.remove('correct'); // Assegura que no tingui la classe 'correct'
  }


  if (selected === correct) {
    feedbackVf.textContent = "Correcte! 🎉";
    feedbackVf.classList.remove('error-text');
    feedbackVf.classList.add('correct-text');
    scoreVf++;
  } else {
    feedbackVf.textContent = `Incorrecte.`; // Simplificat
    feedbackVf.classList.remove('correct-text');
    feedbackVf.classList.add('error-text');
  }

  scoreDisplayVf.textContent = `Puntuació: ${scoreVf}`;

  setTimeout(() => {
    getNewQuestionVf();
  }, 1500);
}

function nextQuestionOrEndVf() {
  if (questionsAskedVf < totalQuestionsVf) {
    getNewQuestionVf();
  } else {
    acabarJocVf();
  }
}

function acabarJocVf() {
  clearInterval(timerIntervalVf);
  stopSaveStatusVf();
  jocVf.style.display = "none";
  resultatVf.style.display = "block";
  missatgeFinalVf.textContent = `Has aconseguit ${scoreVf} de ${totalQuestionsVf} preguntes correctes.`;

  // Aquí pots afegir la lògica per enviar la puntuació al servidor si la vols mantenir
  $.ajax({
    url: "https://fun.codelearn.cat/hackathon/game/finalize",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      game_id: game_id_vf,
      data: {},
      score: scoreVf,
    }),
    success: function (data, textStatus, jqXHR) {
      console.log("Informació de Veritat o Fals guardada correctament");
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error("Error en finalitzar de la partida de Veritat o Fals: " + textStatus);
    },
  });
}

function reiniciarJocVf() {
  clearInterval(timerIntervalVf);
  scoreVf = 0;
  questionsAskedVf = 0;
  scoreDisplayVf.textContent = `Puntuació: 0`;
  progressDisplayVf.textContent = `Pregunta 0 de 0`;
  resultatVf.style.display = "none";
  formulariVf.style.display = "block";
  feedbackVf.textContent = "";
  feedbackVf.classList.remove('correct-text', 'error-text');
  cronoVf.textContent = "";
  stopSaveStatusVf(); // Assegura't de parar el guardat d'estat
}

function tornarAlMenuVf() {
  clearInterval(timerIntervalVf);
  stopSaveStatusVf();
  scoreVf = 0;
  questionsAskedVf = 0;
  scoreDisplayVf.textContent = `Puntuació: 0`;
  progressDisplayVf.textContent = `Pregunta 0 de 0`;
  feedbackVf.textContent = "";
  feedbackVf.classList.remove('correct-text', 'error-text');
  cronoVf.textContent = "";

  jocVf.style.display = "none";
  resultatVf.style.display = "none";
  formulariVf.style.display = "block"; // Tornem al formulari d'inici del joc V/F
}

// Listener per al formulari de configuració del joc
document.getElementById("configuracioJocVf").addEventListener("submit", (e) => {
  e.preventDefault();
  // newGameRequestVf(); // Activar si necessites la petició al servidor al començar
  startSaveStatusVf(); // Activar si vols guardar el progrés

  const dificultat = document.getElementById("dificultatVf").value;
  if (dificultat === "facil") totalQuestionsVf = 10;
  else if (dificultat === "mitja") totalQuestionsVf = 15;
  else if (dificultat === "dificil") totalQuestionsVf = 20;

  if (totalQuestionsVf > questionsVf.length) {
    totalQuestionsVf = questionsVf.length;
    alert(
      `Només hi ha ${questionsVf.length} preguntes de Veritat o Fals disponibles. El joc es configurarà amb aquesta quantitat.`
    );
  }

  questionsPoolVf = shuffleArray(questionsVf).slice(0, totalQuestionsVf);

  formulariVf.style.display = "none";
  resultatVf.style.display = "none";
  jocVf.style.display = "block";

  scoreVf = 0;
  questionsAskedVf = 0;
  scoreDisplayVf.textContent = `Puntuació: 0`;
  progressDisplayVf.textContent = `Pregunta 0 de 0`;
  feedbackVf.textContent = "";
  feedbackVf.classList.remove('correct-text', 'error-text');
  getNewQuestionVf();
});

// Listeners per als botons de tornar al menú
tornarMenuJocVfBtn.addEventListener("click", tornarAlMenuVf);
tornarMenuResultatVfBtn.addEventListener("click", tornarAlMenuVf);

// Funcions per a la comunicació amb el servidor (adapta-les si cal)
function newGameRequestVf() {
  $.ajax({
    url: "https://fun.codelearn.cat/hackathon/game/new",
    method: "GET",
    success: function (data, textStatus, jqXHR) {
      if (jqXHR.status === 200) {
        game_id_vf = data["game_id"];
        seed_vf = data["seed"];
      } else {
        console.error("Error en la creació de la partida de Veritat o Fals: status " + jqXHR.status);
        reiniciarJocVf();
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error("Error en la creació de la partida de Veritat o Fals: " + textStatus);
      reiniciarJocVf();
    },
  });
}

function startSaveStatusVf() {
  if (intervalStatusVf) return;
  intervalStatusVf = setInterval(() => {
    $.ajax({
      url: "https://fun.codelearn.cat/hackathon/game/store_progress",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        game_id: game_id_vf,
        data: { preguntesRespongudes: questionsAskedVf },
      }),
      success: function (data, textStatus, jqXHR) {
        console.log("Informació de Veritat o Fals guardada correctament");
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.error("Error en guardar progrés de la partida de Veritat o Fals: " + textStatus);
      },
    });
  }, 15000);
}

function stopSaveStatusVf() {
  clearInterval(intervalStatusVf);
  intervalStatusVf = null;
}