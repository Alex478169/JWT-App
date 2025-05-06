CREATE DATABASE job_applications;
USE job_applications;

-->creazione tabella job_applications
CREATE TABLE job_application(
    Id_job int generated always as identity,
    application_date varchar(255),
    contact_email varchar(255),
    company_name varchar(255),
    job_title varchar(255),
    job_url varchar(255)
);

-->creazione tabella users
CREATE TABLE users(
    Id_users int generated always as identity,
    username varchar(255),
    passwd varchar(255)
);