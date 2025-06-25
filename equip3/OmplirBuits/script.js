const formulari = document.getElementById("configuracioJoc");
const seccioFormulari = document.getElementById("formulari");
const seccioJoc = document.getElementById("joc");
const seccioResultat = document.getElementById("resultat");
const preguntaBuitDiv = document.getElementById("preguntaBuit");
const zonaElements = document.getElementById("zonaElements");
const crono = document.getElementById("crono");
const missatgeFinal = document.getElementById("missatgeFinal");
const tempsRestantDisplay = document.getElementById("tempsRestant");
const segonsRestantsSpan = document.getElementById("segonsRestants");
const btnNoHoSe = document.getElementById("btnNoHoSe");

let puntuacio = 0;
let intents = 0;
let preguntesFetes = 0;
let preguntesTotals = 5;
let tipusPregunta = "both";
let tempsLimitPerPregunta = 0;

let game_id = 0;
let seed = 0;

let seconds = 0;
let interval = null;
let intervalStatus = null;

let tempsActualPregunta = 0;
let intervalTempsPregunta = null;

const preguntesOmplirBuits = [
  {
    id: 1,
    text: "El primer element de la taula periòdica és l'_HIDROGEN_, que té un _PROTÓ_ al seu nucli. És el més _LLEUGER_ de tots els elements.",
    respostes: ["Hidrogen", "Protó", "Lleuger"],
    tipus: "drag",
    extraElements: ["Heli", "Electró", "Pesat", "Neutró", "Àtom"],
  },
  {
    id: 2,
    text: "La taula periòdica es va organitzar inicialment segons la massa _ATÒMICA_, però _MENDELEEV_ la va ordenar de manera que elements amb propietats _SIMILARS_ quedessin en el mateix _GRUP_.",
    respostes: ["Atòmica", "Mendeleev", "Similars", "Grup"],
    tipus: "type",
    extraElements: [],
  },
  {
    id: 3,
    text: "Els elements del Grup 1 són els metalls _ALCALINS_, i els del Grup 2 són els _ALCALINOTERRIS_. Tots són molt _REACTIUS_ amb l'aigua.",
    respostes: ["Alcalins", "Alcalinoterris", "Reactius"],
    tipus: "both",
    extraElements: ["Gasos Nobles", "Halògens", "Inerts", "Semimetalls", "Estables"],
  },
  {
    id: 4,
    text: "L'_OXIGEN_ és un element essencial per a la _VIDA_ i forma part de la molècula d'_AIGUA_ (H2O).",
    respostes: ["Oxigen", "Vida", "Aigua"],
    tipus: "drag",
    extraElements: ["Nitrogen", "Mort", "Foc", "Carboni", "Terra"],
  },
  {
    id: 5,
    text: "El símbol 'Au' representa l'_OR_, un metall _PRECIÓS_ i molt _MALLEABLE_. 'Ag' és la _PLATA_.",
    respostes: ["Or", "Preciós", "Malleable", "Plata"],
    tipus: "type",
    extraElements: [],
  },
  {
    id: 6,
    text: "Els gasos nobles, com l'_HELI_ i el _NEÓ_, són coneguts per la seva baixa _REACTIVITAT_ química, ja que tenen la seva última capa d'electrons _COMPLETA_.",
    respostes: ["Heli", "Neó", "Reactivitat", "Completa"],
    tipus: "both",
    extraElements: ["Xenó", "Fluor", "Densitat", "Buida", "Argó", "Incompleta"],
  },
  {
    id: 7,
    text: "El _FERRO_ (Fe) és un metall de _TRANSICIÓ_ i és un component clau en la producció d'_ACER_. És un dels elements més _ABUNDANTS_ a la Terra.",
    respostes: ["Ferro", "Transició", "Acer", "Abundants"],
    tipus: "drag",
    extraElements: ["Coure", "Alcalí", "Bronze", "Rars", "Or", "Dúctil"],
  },
  {
    id: 8,
    text: "Els _HALÒGENS_ (Grup 17), com el _CLOR_ i el _IODE_, són molt _REACTIUS_ i formen compostos amb la majoria d'elements. Sovint s'utilitzen com a _DESINFECTANTS_.",
    respostes: ["Halògens", "Clor", "Iode", "Reactius", "Desinfectants"],
    tipus: "both",
    extraElements: ["Calcógenos", "Sofre", "Brom", "Estables", "Aïllants", "Neutres", "Àcids"],
  },
  {
    id: 9,
    text: "El _CARBONI_ és la base de la química _ORGÀNICA_ i pot formar _CADENES_ llargues. És present en formes al·lotròpiques com el _DIAMANT_ i el grafit.",
    respostes: ["Carboni", "Orgànica", "Cadenes", "Diamant"],
    tipus: "type",
    extraElements: [],
  },
  {
    id: 10,
    text: "El _SILICI_ és un _SEMIMETALL_ i és el segon element més _ABUNDANT_ a l'escorça terrestre. És fonamental en la indústria _ELECTRÒNICA_.",
    respostes: ["Silici", "Semimetall", "Abundant", "Electrònica"],
    tipus: "drag",
    extraElements: ["Germani", "Metall", "Rar", "Mecànica", "Fust", "Aïllant"],
  },
  {
    id: 11,
    text: "El _FÒSFOR_ és un _NO-METALL_ vital per a la vida i es troba a l'ADN. El _SOFRE_ és un altre no-metall de color groc.",
    respostes: ["Fòsfor", "No-metall", "Sofre"],
    tipus: "both",
    extraElements: ["Arsènic", "Metall", "Clor", "Bismut", "Tel·luri"],
  },
  {
    id: 12,
    text: "Els _LANTÀNIDS_ i _ACTÍNIDS_ són metalls de _TRANSICIÓ_ interns. Els _ACTÍNIDS_ són tots _RADIOACTIUS_.",
    respostes: ["Lantànids", "Actínids", "Transició", "Actínids", "Radioactius"],
    tipus: "both",
    extraElements: ["Alcalins", "Halògens", "Principals", "Estables", "Metalls pesants", "Actius"],
  },
  {
    id: 13,
    text: "La _MASSA_ atòmica es mesura en unitats de massa atòmica (_UMA_). El nombre _ATÒMIC_ (Z) és el nombre de _PROTONS_ en un àtom.",
    respostes: ["Massa", "uma", "Atòmic", "Protons"],
    tipus: "type",
    extraElements: [],
  },
  {
    id: 14,
    text: "L'element amb el símbol _Na_ és el _SODI_, un metall alcalí que reacciona violentament amb l'_AIGUA_.",
    respostes: ["Na", "Sodi", "aigua"],
    tipus: "drag",
    extraElements: ["Cl", "Potassi", "Foc", "Liti", "Aire"],
  },
  {
    id: 15,
    text: "Els elements del Grup 13 són els _BOROIDES_, i els del Grup 14 són els _CARBONOIDES_. El _SILICI_ pertany a aquest darrer grup.",
    respostes: ["Boroides", "Carbonoides", "Silici"],
    tipus: "both",
    extraElements: ["Nitrogenoides", "Oxigenoides", "Germani", "Estany"],
  },
];

formulari.addEventListener("submit", (e) => {
  e.preventDefault();

  const dificultat = document.getElementById("dificultat").value;
  tipusPregunta = document.getElementById("tipusPregunta").value;
  tempsLimitPerPregunta = parseInt(document.getElementById("tempsLimit").value);

  iniciarJoc(dificultat);
});

let preguntesActuals = [];
let buitsActuals = [];

btnNoHoSe.addEventListener("click", saltarPregunta);

function iniciarJoc(dificultat) {
  newGameRequest();
  startSaveStatus();

  puntuacio = 0;
  intents = 0;
  preguntesFetes = 0;
  preguntaBuitDiv.innerHTML = "";
  zonaElements.innerHTML = "";
  seccioFormulari.style.display = "none";
  seccioJoc.style.display = "block";
  seccioResultat.style.display = "none";

  seconds = 0;
  startTimer();

  const nombrePreguntes = {
    facil: 5,
    mitja: 7,
    dificil: 10,
  }[dificultat];

  preguntesTotals = nombrePreguntes;

  const preguntesFiltrades = preguntesOmplirBuits.filter((q) => {
    if (tipusPregunta === "both") return true;
    return q.tipus === tipusPregunta;
  });

  const preguntesBarrejades = [...preguntesFiltrades].sort(
    () => Math.random(seed) - 0.5
  );
  preguntesActuals = preguntesBarrejades.slice(0, preguntesTotals);

  carregarPregunta();
}

function carregarPregunta() {
  if (preguntesFetes >= preguntesTotals) {
    finalitzarJoc();
    return;
  }

  stopTempsPregunta();

  preguntaBuitDiv.innerHTML = "";
  zonaElements.innerHTML = "";
  buitsActuals = [];

  const pregunta = preguntesActuals[preguntesFetes];
  preguntesFetes++;

  const numeroPregunta = document.createElement("p");
  numeroPregunta.textContent = preguntesFetes + " de " + preguntesTotals;
  crono.replaceChildren(numeroPregunta);

  const partsFrase = pregunta.text.split(/_([^_]+)_/g);

  partsFrase.forEach((part, index) => {
    if (index % 2 === 1) {
      const buit = document.createElement("span");
      buit.className = "buit";
      buit.dataset.respostaCorrecta = part.toLowerCase();
      buit.dataset.estat = "pendent";
      buit.dataset.originalContent = part;

      if (pregunta.tipus === "type" || pregunta.tipus === "both") {
        const input = document.createElement("input");
        input.type = "text";
        input.placeholder = "_______";
        input.addEventListener("change", (e) =>
          comprovarRespostaEscrita(e, buit)
        );
        buit.appendChild(input);
      }
      if (pregunta.tipus === "drag" || pregunta.tipus === "both") {
        buit.textContent = "";
        buit.addEventListener("dragover", (e) => {
          e.preventDefault();
          if (buit.dataset.estat === "pendent") {
            buit.classList.add("dragover");
          }
        });
        buit.addEventListener("dragleave", () => {
          buit.classList.remove("dragover");
        });
        buit.addEventListener("drop", (e) => comprovarRespostaArrossegar(e, buit));
      }
      preguntaBuitDiv.appendChild(buit);
      buitsActuals.push(buit);
    } else {
      const span = document.createElement("span");
      span.className = "buit-text";
      span.textContent = part;
      preguntaBuitDiv.appendChild(span);
    }
  });

  if (pregunta.tipus === "drag" || pregunta.tipus === "both") {
    let elementsDisponibles = [...pregunta.respostes];
    if (pregunta.extraElements && pregunta.extraElements.length > 0) {
      elementsDisponibles = elementsDisponibles.concat(pregunta.extraElements);
    }

    const barrejatsPerArrossegar = [...elementsDisponibles].sort(
      () => Math.random(seed) - 0.5
    );

    barrejatsPerArrossegar.forEach((res) => {
      const element = document.createElement("div");
      element.className = "element draggable";
      element.textContent = res;
      element.setAttribute("draggable", true);
      element.dataset.valor = res.toLowerCase();
      zonaElements.appendChild(element);
    });

    activarDrag();
  }

  btnNoHoSe.style.display = "block";

  if (tempsLimitPerPregunta > 0) {
    tempsActualPregunta = tempsLimitPerPregunta;
    segonsRestantsSpan.textContent = tempsActualPregunta;
    tempsRestantDisplay.style.display = "block";
    intervalTempsPregunta = setInterval(() => {
      tempsActualPregunta--;
      segonsRestantsSpan.textContent = tempsActualPregunta;
      if (tempsActualPregunta <= 0) {
        clearInterval(intervalTempsPregunta);
        saltarPregunta();
      }
    }, 1000);
  } else {
    tempsRestantDisplay.style.display = "none";
  }
}

function stopTempsPregunta() {
  clearInterval(intervalTempsPregunta);
  intervalTempsPregunta = null;
}

function activarDrag() {
  const elements = document.querySelectorAll(".element.draggable");
  elements.forEach((el) => {
    el.addEventListener("dragstart", (e) => {
      e.dataTransfer.setData("text/plain", el.dataset.valor);
      e.dataTransfer.setData("text/name", el.textContent);
    });
  });
}

function comprovarRespostaEscrita(event, buit) {
  if (buit.dataset.estat === "correcte") return;

  const valorInput = event.target.value.toLowerCase().trim();
  const respostaCorrecta = buit.dataset.respostaCorrecta.toLowerCase();

  intents++;

  if (valorInput === respostaCorrecta) {
    buit.classList.add("encert");
    buit.dataset.estat = "correcte";
    event.target.readOnly = true;
    event.target.value = buit.dataset.originalContent;
    puntuacio++;
  } else {
    buit.classList.add("error");
    setTimeout(() => {
      buit.classList.remove("error");
      event.target.value = "";
    }, 1000);
  }
  comprovarPreguntaCompleta();
}

function comprovarRespostaArrossegar(e, buit) {
  e.preventDefault();
  buit.classList.remove("dragover");

  if (buit.dataset.estat === "correcte") return;

  const valorArrossegat = e.dataTransfer.getData("text/plain").toLowerCase();
  const nomArrossegat = e.dataTransfer.getData("text/name");
  const respostaCorrecta = buit.dataset.respostaCorrecta.toLowerCase();
  const elementDraggable = document.querySelector(
    `.element.draggable[data-valor="${valorArrossegat}"]`
  );

  intents++;

  if (valorArrossegat === respostaCorrecta) {
    buit.classList.add("encert");
    buit.dataset.estat = "correcte";
    buit.textContent = nomArrossegat;

    puntuacio++;

    if (elementDraggable) {
      elementDraggable.classList.add("desactived");
      elementDraggable.setAttribute("draggable", false);
    }
  } else {
    buit.classList.add("error");
    setTimeout(() => {
      buit.classList.remove("error");
      buit.textContent = "";
    }, 1000);
  }
  comprovarPreguntaCompleta();
}

function comprovarPreguntaCompleta() {
  let totsCorrectes = true;
  buitsActuals.forEach((buit) => {
    if (buit.dataset.estat !== "correcte") {
      totsCorrectes = false;
    }
  });

  if (totsCorrectes) {
    stopTempsPregunta();
    setTimeout(() => {
      carregarPregunta();
    }, 500);
  }
}

function saltarPregunta() {
    stopTempsPregunta();

    buitsActuals.forEach(buit => {
        if (buit.dataset.estat === "pendent") {
            buit.classList.remove("encert");
            buit.classList.add("error");
            
            if (buit.querySelector('input')) {
                const input = buit.querySelector('input');
                input.value = buit.dataset.originalContent;
                input.readOnly = true;
            } else {
                buit.textContent = buit.dataset.originalContent;
                const elementDraggable = document.querySelector(`.element.draggable[data-valor="${buit.dataset.respostaCorrecta.toLowerCase()}"]`);
                if (elementDraggable && !elementDraggable.classList.contains("desactived")) {
                  elementDraggable.classList.add("desactived");
                  elementDraggable.setAttribute("draggable", false);
                }
            }
            buit.dataset.estat = "saltada";
        }
    });

    const currentInputs = preguntaBuitDiv.querySelectorAll('input');
    currentInputs.forEach(input => input.readOnly = true);
    const currentDraggables = zonaElements.querySelectorAll('.element.draggable');
    currentDraggables.forEach(el => {
      el.classList.add("desactived");
      el.setAttribute("draggable", false);
    });

    setTimeout(() => {
        carregarPregunta();
    }, 1000);
}

function finalitzarJoc() {
  stopTimer();
  stopSaveStatus();
  stopTempsPregunta();

  const puntuacioFinal = calculaPuntuacio(puntuacio, intents);

  seccioJoc.style.display = "none";
  seccioResultat.style.display = "block";

  const minutes = Math.floor(seconds / 60);
  const secondsDisplay = seconds % 60;
  const formattedSeconds =
    secondsDisplay < 10 ? "0" + secondsDisplay : secondsDisplay;

  missatgeFinal.innerHTML = `
    N'has encertat <strong>${puntuacio}</strong> en <strong>${intents}</strong> intents. </br> Temps total: <strong>${minutes}:${formattedSeconds}</strong>.
    <h1>Puntuació: ${puntuacioFinal}</h1>
  `;

  $.ajax({
    url: "https://fun.codelearn.cat/hackathon/game/finalize",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      game_id: game_id,
      data: { temps: seconds, puntuacioBruta: puntuacio, intentsTotals: intents },
      score: parseFloat(puntuacioFinal.replace("%", "")),
    }),
    success: function (data, textStatus, jqXHR) {
      console.log("Informació guardada correctament", data);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error("Error en finalitzar de la partida: ", textStatus, errorThrown);
      alert("Error en finalitzar de la partida: " + textStatus);
    },
  });
}

function reiniciarJoc() {
  seccioFormulari.style.display = "block";
  seccioJoc.style.display = "none";
  seccioResultat.style.display = "none";
  preguntaBuitDiv.innerHTML = "";
  zonaElements.innerHTML = "";
  buitsActuals = [];
  stopTimer();
  stopTempsPregunta();
}

function tornarEnrereEnJoc() {
  stopTimer();
  stopSaveStatus();
  stopTempsPregunta();
  reiniciarJoc();
}

function startTimer() {
  if (interval) return;
  seconds = 0;
  interval = setInterval(() => {
    seconds++;
  }, 1000);
}

function stopTimer() {
  clearInterval(interval);
  interval = null;
}

function calculaPuntuacio(totalCorrectes, totalIntents) {
  if (totalIntents === 0) {
    return "0.00%";
  }

  let puntuacioPercentatge = (totalCorrectes / totalIntents) * 100;
  puntuacioPercentatge = Math.min(Math.max(puntuacioPercentatge, 0), 100);
  const resultatFormatat = puntuacioPercentatge.toFixed(2);

  return resultatFormatat + "%";
}

function newGameRequest() {
  $.ajax({
    url: "https://fun.codelearn.cat/hackathon/game/new",
    method: "GET",
    success: function (data, textStatus, jqXHR) {
      if (jqXHR.status === 200) {
        game_id = data["game_id"];
        seed = data["seed"];
      } else {
        console.error("Error en la creació de la partida: status " + jqXHR.status);
        alert("Error en la creació de la partida: " + jqXHR.status);
        reiniciarJoc();
      }
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error("Error en la creació de la partida: ", textStatus, errorThrown);
      alert("Error en la creació de la partida: " + textStatus);
      reiniciarJoc();
    },
  });
}

function startSaveStatus() {
  if (intervalStatus) return;
  intervalStatus = setInterval(() => {
    $.ajax({
      url: "https://fun.codelearn.cat/hackathon/game/store_progress",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        game_id: game_id,
        data: { tempsTranscorregut: seconds, puntuacioActual: puntuacio, preguntesActuals: preguntesFetes },
      }),
      success: function (data, textStatus, jqXHR) {
        console.log("Informació de progrés guardada correctament");
      },
      error: function (jqXHR, textStatus, errorThrown) {
        console.error("Error en guardar el progrés de la partida: ", textStatus, errorThrown);
      },
    });
  }, 15000);
}

function stopSaveStatus() {
  clearInterval(intervalStatus);
  intervalStatus = null;
}