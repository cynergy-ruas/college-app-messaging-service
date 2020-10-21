package com.cynergy.Srikanth.model;


import org.springframework.data.annotation.Id; // Used to Declare ID for Mongo DB
import org.springframework.stereotype.Component; // Used to Declare a Component in Spring Boot

@Component
public class schema {
    /* 
    Basically what we are doing here is we are declaring our schema with @ID to mark it with our database  
    and basic getters and setters cause its private declaration.
    */
    @Id
    private String message; 
    private String User;
    private MessageType type;
    private String Channel_Name;
  
    public enum MessageType{
        CHAT,LEAVE,JOIN
    }

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

    public MessageType getType() {
        return type;
    }

    public void setType(MessageType type) {
        this.type = type;
    }

    public String getChannel_Name() {
        return Channel_Name;
    }

    public void setChannel_Name(String channel_Name) {
        Channel_Name = channel_Name;
    }

    
   

    
}
