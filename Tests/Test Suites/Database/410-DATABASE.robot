*** Settings ***
Resource        ../../../robotframework/resource/database.resource


*** Test Cases ***
41001-REQ-CONNEXION-DATABASE
    [Documentation]     Test la connexion à MySQL en étant le root user
    [Tags]              Connexion   Center   Database
    Log                 Connexion à la base de donnée en étant l'utilisateur root

    ${Connexion}=       Vérifier la connexion à MySQL
    Should Be True      ${Connexion}
    Log                 La connexion est réussie
    
    Log                 Montrer toutes les bases de données concernant Onche
    Montrer toutes les bases de donnée de Onche

    Log                 Liste de tous les utilisateurs pour onche
    Montrer tous les utilisateurs MySQL pour Onche

41002-REQ-MANIPULATION-UTILISATEUR
    [Documentation]     Test la connexion à MySQL en étant le root user
    [Tags]              User   Center   Database
    Log                 Vérification des opérations sur les utilisateurs
    ${users}=           Montrer tous les utilisateurs MySQL pour Onche

    Log                 Création de l'utilisateur OncheTest





