package com.cynergy.Srikanth.db;

import com.cynergy.Srikanth.model.schema; // Importing our schema 

import org.springframework.data.mongodb.repository.MongoRepository; // Used to configure our schema to our database.


public interface messagerepo extends MongoRepository<schema,String> {
    /* 
    Okay now this file is where we connect our schema to our database 
    we extend our interface to MongoRepository with our schema and yeah thats it 
    boom our schema is connected with database. 
    so the url key to connect to our databse is in resources/application.properties file 
    and url is declared as Url and the next variable that you see is message and that is our DB name 

    *************************************
     Credentials for Mongo DB

        Username  : mongodb2301@gmail.com
        Password : Srikanth@23
    *************************************
    */
}
