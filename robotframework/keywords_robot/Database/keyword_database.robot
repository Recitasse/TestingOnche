*** Settings ***
Resource        ../../../robotframework/resource/database.resource
Library    Collections

*** Keywords ***
Vérifier que la base de donnée ${database} existe
    [Documentation]     Vérifie qu'une base de donnée donnée existe
    ${databases}=       Montrer toutes les bases de donnée

    List Should Contain Value      ${databases}     ${database}

Vérifier que la base de donnée ${database} n'existe pas
    [Documentation]     Vérifie qu'une base de donnée donnée n'existe pas
    ${databases}=       Montrer toutes les bases de donnée

    List Should Not Contain Value      ${databases}     ${database}

Créer la base de donnée de test
    [Documentation]     Créer la base de donnée de test temporaire
    ${database}=        OncheTest

    Créer la base de donnée ${database}
    Vérifier que la base de donnée ${database} existe

Effacer la base de donnée de test
    [Documentation]     Efface la base de donnée de test temporaire
    ${database}=        OncheTest

    Efface la base de donnée ${database}
    Vérifier que la base de donnée ${database} n'existe pas