*** Settings ***
Suite Setup       Connect To Database    psycopg2    ${DBName}    ${DBUser}    ${DBPass}    ${DBHost}    ${DBPort}
Suite Teardown    Disconnect From Database
Library           DatabaseLibrary
Library           OperatingSystem
Library           Collections

*** Variables ***
${DBHost}         localhost
${DBName}         Onche
${DBPass}         ""
${DBPort}         5432
${DBUser}         postgres
