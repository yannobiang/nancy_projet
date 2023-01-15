
def estimation(montant, pays):

    euro = 656
    
    if pays == "france" and montant > 4800:
        return "Entrer un montant inferieur à 4800 euros"
    elif montant > 3200000 and pays == "gabon":
        return "Entre un montant inferieur à 3.2 millions"
    elif pays is None and montant is None :
        return "Choisi un pays et un montant"
    else :
        if pays == "france":
            





if (send_button != null) {
  send_button.addEventListener("click", () => {
    const pays = document.getElementById("pays").value;
    const expr = document.getElementById("montant").value;

    if (pays == "france" && eval(expr) > 3000 && expr.length > 0) {
      alert("Entrer un montant inferieur à 3000 € !");
      estimateur.style.display = "none";
      cont2.style.display = "none";
      cont3.style.display = "none";
      acceuil.style.display = "block";
      letitre.style.display = "none";
      paint.style.width = "35%";
      contents.style.width = "65%";

      // images
      image1.style.display = "block";
      image2.style.display = "block";

      image3.style.display = "block";
      image5.style.display = "block";
      image7.style.display = "block";
      image8.style.display = "block";
      image6.style.display = "block";
      image9.style.display = "block";
    } else if (pays.length == 0 || expr.length == 0 || expr == 0) {
      alert("Choisis un pays et un montant");
      estimateur.style.display = "none";
      cont2.style.display = "none";
      cont3.style.display = "none";
      acceuil.style.display = "block";
      letitre.style.display = "none";
      paint.style.width = "35%";
      contents.style.width = "65%";

      // images

      image1.style.display = "block";
      image2.style.display = "block";

      image3.style.display = "block";
      image5.style.display = "block";
      image7.style.display = "block";
      image8.style.display = "block";
      image6.style.display = "block";
      image9.style.display = "block";
    } else if (eval(expr) > 3200000 && pays == "gabon") {
      alert("Entrer un montant inferieur à 1 million de Franc CFA !");
      letitre.style.display = "none";
      estimateur.style.display = "none";
      acceuil.style.display = "block";
      cont2.style.display = "none";
      cont3.style.display = "none";
      paint.style.width = "35%";
      contents.style.width = "65%";

      // images

      image1.style.display = "block";
      image2.style.display = "block";

      image3.style.display = "block";
      image5.style.display = "block";
      image7.style.display = "block";
      image8.style.display = "block";
      image6.style.display = "block";
      image9.style.display = "block";
    } else {
      /* Ajout de code ici
      
      
    body.style.overflowY = "visible";
    cont3.style.display = "flex";
    cont3.style.flexDirection = "row";
    cont2.style.margin = "10px 0px 20px 1000px";

    bulle.style.display = "none";
    /*cont1.style.flexDirection = "column";*/
      acceuil.style.display = "none";
      cont2.style.display = "flex";
      cont2.style.flexDirection = "column";
      cont2.style.color = "white";
      cont2.style.fontWeight = "bold";
      cont2.style.margin = "10px 5px 20px 2px";
      cont3.style.display = "flex";
      cont3.style.flexDirection = "row";
      cont3.style.justifyContent = "center;";
      estimateur.style.display = "block";
      letitre.style.display = "block";
      paint.style.width = "65%";
      contents.style.width = "35%";

      // images

      image1.style.display = "none";
      image2.style.display = "none";

      image3.style.display = "none";
      image5.style.display = "none";
      image7.style.display = "none";
      image8.style.display = "none";
      image6.style.display = "none";
      image9.style.display = "none";

      // fin add images

      const euro = 656;
      let com = 0;
      let com2 = 0;
      let airtelSansFrais = 0;
      let mainPropre = 0;
      let airAvecFrais = 0;

      if (pays == "gabon") {
        /*commission un pour les transfert airtel */
        switch (true) {
          case eval(expr) <= 1000:
            com = 50;
            break;
          case eval(expr) > 1000 && eval(expr) <= 5000:
            com = 100;
            break;
          case eval(expr) > 5000 && eval(expr) <= 10000:
            com = 100;
            break;

          case eval(expr) > 10000 && eval(expr) <= 20000:
            com = 200;
            break;

          case eval(expr) > 20000 && eval(expr) <= 30000:
            com = 300;
            break;

          case eval(expr) > 30000 && eval(expr) <= 40000:
            com = 400;
            break;

          case eval(expr) > 40000 && eval(expr) <= 60000:
            com = 600;
            break;

          case eval(expr) > 60000 && eval(expr) <= 100000:
            com = 800;
            break;

          case eval(expr) > 100000 && eval(expr) <= 500000:
            com = 1500;
            break;

          case eval(expr) > 500000 && eval(expr) <= 1000000:
            com = 2500;
            break;

          case eval(expr) > 1000000 && eval(expr) <= 2000000:
            com = 3500;
            break;
          case eval(expr) > 2000000 && eval(expr) < 3500000:
            com = ((eval(expr) + 500000) / 500000) * 500 + 3500;
            break;

          default:
            alert(
              "Veuillez entrer une somme inferieur à 3.5 millions de Franc CFA"
            );
        }

        /* ici le cas de la deuxieme commission */

        switch (true) {
          case eval(expr) > 0 && eval(expr) <= 100000:
            com2 = 3000;
            break;
          case eval(expr) > 100000 && eval(expr) <= 200000:
            com2 = 1500 + 3000;
            break;
          case eval(expr) > 200000 && eval(expr) <= 300000:
            com2 = eval(1500 * 2) + 3000;
            break;
          case eval(expr) > 300000 && eval(expr) <= 400000:
            com2 = eval(1500 * 3) + 3000;
            break;
          case eval(expr) > 400000 && eval(expr) <= 500000:
            com2 = eval(1500 * 4) + 3000;
            break;
          case eval(expr) > 500000 && eval(expr) <= 600000:
            com2 = eval(1500 * 5) + 3000;
            break;
          case eval(expr) > 600000 && eval(expr) <= 700000:
            com2 = eval(1500 * 6) + 3000;
            break;
          case eval(expr) > 700000 && eval(expr) <= 800000:
            com2 = eval(1500 * 7) + 3000;
            break;
          case eval(expr) > 800000 && eval(expr) <= 900000:
            com2 = eval(1500 * 8) + 3000;
            break;
          case eval(expr) > 900000 && eval(expr) <= 1000000:
            com2 = eval(1500 * 9) + 3000;
            break;
          case eval(expr) > 1000000 && eval(expr) <= 1100000:
            com2 = eval(1500 * 10) + 3000;
            break;
          case eval(expr) > 1100000 && eval(expr) <= 1200000:
            com2 = eval(1500 * 11) + 3000;
            break;
          case eval(expr) > 1200000 && eval(expr) <= 1300000:
            com2 = eval(1500 * 12) + 3000;
            break;
          case eval(expr) > 1300000 && eval(expr) <= 1400000:
            com2 = eval(1500 * 13) + 3000;
            break;
          case eval(expr) > 1400000 && eval(expr) <= 1500000:
            com2 = eval(1500 * 14) + 3000;
            break;
          case eval(expr) > 1500000 && eval(expr) <= 1600000:
            com2 = eval(1500 * 15) + 3000;
            break;
          case eval(expr) > 1600000 && eval(expr) <= 1700000:
            com2 = eval(1500 * 16) + 3000;
            break;
          case eval(expr) > 1700000 && eval(expr) <= 1800000:
            com2 = eval(1500 * 17) + 3000;
            break;
          case eval(expr) > 1800000 && eval(expr) <= 1900000:
            com2 = eval(1500 * 18) + 3000;
            break;
          case eval(expr) > 1900000 && eval(expr) <= 2000000:
            com2 = eval(1500 * 19) + 3000;
            break;
          case eval(expr) > 2000000:
            com2 = ((eval(expr) + 100000) / 100000) * 1500 + 3000;
            break;

          default:
            console.log("Je ne peux calculer la seconde commission");
        }
        airtelSansFrais = Math.round(eval(expr) + eval(com2)).toFixed(2);
        airAvecFrais = Math.round(eval(expr) + eval(com) + eval(com2)).toFixed(
          2
        );
        mainPropre = Math.round(eval(expr) + eval(com2)).toFixed(2);
        letitre.innerHTML =
          "Trandfert de La France vers Le " +
          pays +
          " de " +
          expr +
          " Franc CFA";

        let informations = [
          {
            Type: "Airtel-sans-frais",
            "Montant-TTC en CFA": airtelSansFrais,
            "Montant-TTC en €": Math.round(
              eval(airtelSansFrais / euro)
            ).toFixed(2),
            "Total-commission en CFA": eval(com2),
            "Tatal-commission en €": Math.round(eval(com2) / euro).toFixed(2),
          },

          {
            Type: "Airtel-avec-frais",
            "Montant-TTC en CFA": airAvecFrais,
            "Montant-TTC en €": Math.round(eval(airAvecFrais / euro)).toFixed(
              2
            ),
            "Total-commission en CFA": eval(com) + eval(com2),
            "Total-commission en €": Math.round(
              eval(eval(com) / euro + eval(com2) / euro)
            ).toFixed(2),
          },

          {
            Type: "Récuperer en main",
            "Montant-TTC en CFA": mainPropre,
            "Montant-TTC en €": Math.round(eval(mainPropre) / euro).toFixed(2),
            "Tatal-commission en CFA": eval(com2),
            "Total-commission en €": Math.round(eval(com2) / euro).toFixed(2),
          },
        ];
        const table = document.querySelector("table");
        if (table.rows.length == 0) {
          console.log("je suis vide");
          let data = Object.keys(informations[0]);
          generateTableHead(table, data);
          generateTable(table, informations);
        } else {
          console.log("je ne suis donc plus vide");
        }
      } else if (pays == "france") {
        switch (true) {
          case eval(expr) <= Math.round(1000 / euro).toFixed(2):
            com = Math.round(50 / euro).toFixed(2);
            break;
          case eval(expr) > Math.round(1000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(5000 / euro).toFixed(2):
            com = Math.round(100 / euro).toFixed(2);
            break;
          case eval(expr) > Math.round(5000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(10000 / euro).toFixed(2):
            com = Math.round(100 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(10000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(20000 / euro).toFixed(2):
            com = Math.round(200 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(20000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(30000 / euro).toFixed(2):
            com = Math.round(300 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(30000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(40000).toFixed(2):
            com = Math.round(400 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(40000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(60000 / euro).toFixed(2):
            com = Math.round(600 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(60000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(100000 / euro).toFixed(2):
            com = Math.round(800 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(100000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(500000 / euro).toFixed(2):
            com = Math.round(1500 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(500000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(1000000 / euro).toFixed(2):
            com = Math.round(2500 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(1000000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(2000000 / euro).toFixed(2):
            com = Math.round(2500 / euro).toFixed(2);
            break;

          default:
            alert("Veuillez entrer une somme inferieur à 3 000 €");
            break;
        }

        /* ici le cas de la deuxieme commission */
        switch (true) {
          case eval(expr) <= Math.round(eval(60000 / euro)).toFixed(2):
            com2 = Math.round(500 / euro).toFixed(2);

            break;
          case eval(expr) > Math.round(60000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(90000 / euro).toFixed(2):
            com2 = Math.round(700 / euro).toFixed(2);

            break;
          case eval(expr) > Math.round(90000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(120000 / euro).toFixed(2):
            com2 = Math.round(900 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(120000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(150000 / euro).toFixed(2):
            com2 = Math.round(1100 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(150000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(300000 / euro).toFixed(2):
            com2 = Math.round(1300 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(300000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(400000 / euro).toFixed(2):
            com2 = Math.round(1500 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(400000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(600000 / euro).toFixed(2):
            com2 = Math.round(1900 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(600000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(1000000 / euro).toFixed(2):
            com2 = Math.round(2300 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(1000000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(1500000 / euro).toFixed(2):
            com2 = Math.round(2700 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(1500000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(2000000 / euro).toFixed(2):
            com2 = Math.round(3100 / euro).toFixed(2);
            break;

          case eval(expr) > Math.round(2000000 / euro).toFixed(2) &&
            eval(expr) <= Math.round(3000000 / euro).toFixed(2):
            com2 = Math.round(3500 / euro).toFixed(2);
            break;

          default:
            alert("Pas de transfert au dessus de 3000 €");
        }

        airtelSansFrais = Math.round(eval(expr) + eval(com2)).toFixed(2);
        airAvecFrais = Math.round(
          eval(expr) + (eval(com) + eval(com2))
        ).toFixed(2);
        mainPropre = Math.round(eval(expr) + eval(com2)).toFixed(2);

        letitre.innerHTML =
          "Trandfert du Gabon vers La " + pays + " de " + expr + " €";

        let informations = [
          {
            Type: "Airtel-sans-frais",
            "Montant-TTC en €": airtelSansFrais,
            "Montant-TTC en CFA": Math.round(
              eval(airtelSansFrais * euro)
            ).toFixed(2),
            "Total-commission en €": eval(com2),
            "Tatal-commission en CFA": Math.round(eval(com2) * euro).toFixed(2),
          },

          {
            Type: "Airtel-avec-frais",
            "Montant-TTC en €": airAvecFrais,
            "Montant-TTC en CFA": Math.round(eval(airAvecFrais * euro)).toFixed(
              2
            ),
            "Total-commission en €": eval(com) + eval(com2),
            "Total-commission en CFA": Math.round(
              eval(eval(com) * euro + eval(com2) * euro)
            ).toFixed(2),
          },

          {
            Type: "Récuperer en main",
            "Montant-TTC en €": mainPropre,
            "Montant-TTC en CFA": Math.round(eval(mainPropre) * euro).toFixed(
              2
            ),
            "Tatal-commission en €": eval(com2),
            "Total-commission en CFA": Math.round(eval(com2) * euro).toFixed(2),
          },
        ];
        const table = document.querySelector("table");
        if (table.rows.length == 0) {
          console.log("je suis vide");
          let data = Object.keys(informations[0]);
          generateTableHead(table, data);
          generateTable(table, informations);
        } else {
          console.log("je ne suis donc plus vide");
        }
      }
    }
  });
}
