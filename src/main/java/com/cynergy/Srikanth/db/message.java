package com.cynergy.Srikanth.db;

import com.cynergy.Srikanth.model.schema.MessageType; 

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document
public class message {
    
    @Id
    private String message; 
    private String User;
    // private MessageType type;
    private String Channel_Name;
    //private Date date; 
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getUser() {
        return User;
    }

    public void setUser(String user) {
        User = user;
    }

    // public MessageType getType() {
    //     return type;
    // }

    // public void setType(MessageType type) {
    //     this.type = type;
    // }

    public String getChannel_Name() {
        return Channel_Name;
    }

    public void setChannel_Name(String channel_Name) {
        Channel_Name = channel_Name;
    }



    



}
