package com.cynergy.Srikanth.db;

import org.springframework.data.mongodb.repository.MongoRepository;


public interface messagerepo extends MongoRepository<message,String> {
    
}
