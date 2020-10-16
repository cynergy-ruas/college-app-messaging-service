package com.cynergy.Srikanth.model;
import java.sql.Timestamp;    
import java.util.Date;    
public class schema {

    private String message; 
    private String User;
    private MessageType type;
    private String Channel_Name;
    private Date date; 

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

    public Date getDate() {
         
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }
    

   

    
}
