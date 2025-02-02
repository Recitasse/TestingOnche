*** Settings ***
Resource        ../../../robotframework/resource/database.resource
Library    Collections

*** Keywords ***
Vérifier que l'utilisateur ${user} existe
    [Documentation]     Vérifie bien que l'utilisateur ${user} existe bien
    ${users}=           Montrer tous les utilisateurs MySQL pour Onche
    List Should Contain Value   ${users}    ${user}

Vérifier que l'utilisateur ${user} n'existe pas
    [Documentation]     Vérifie bien que l'utilisateur ${user} n'existe pas
    ${users}=           Montrer tous les utilisateurs MySQL pour Onche
    List Should Not Contain Value   ${users}    ${user}