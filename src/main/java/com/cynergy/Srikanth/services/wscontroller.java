package com.cynergy.Srikanth.services;

import com.cynergy.Srikanth.model.schema;

import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.simp.SimpMessageHeaderAccessor;
import org.springframework.stereotype.Controller;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
@Controller
public class wscontroller {


    @MessageMapping("/chat.channel")
    @SendTo("/channel/public")
    public schema register(@Payload schema chatMessage,SimpMessageHeaderAccessor headerAccessor){ 
        headerAccessor.getSessionAttributes().put("Channel",chatMessage.getUser());
        return chatMessage;
    }

     /* 
    TO CREATE USER IN THE CHANNEL 
    */

    @MessageMapping("/chat.send")
    @SendTo("/channel/public")
    public schema sendmessage(@Payload schema chatMessage){
        return chatMessage;
    }

    /* 
    TO SEND MESSAGES
    */


    }


    

