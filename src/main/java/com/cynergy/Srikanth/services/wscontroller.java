package com.cynergy.Srikanth.services;

import com.cynergy.Srikanth.model.schema;

import org.springframework.messaging.handler.annotation.Payload; // Used to Declare payload
import org.springframework.messaging.simp.SimpMessageHeaderAccessor; // Used to SimpMessageHeaderAccesso
import org.springframework.stereotype.Controller; // Used to Declare Controller
import org.springframework.messaging.handler.annotation.MessageMapping; // Used to Declare a annotation for message mapping
import org.springframework.messaging.handler.annotation.SendTo; // Used to Declare a annotation send to
@Controller
public class wscontroller {

    @MessageMapping("/chat.channel") // Used Map the url from client and server
    @SendTo("/channel/public") // Used to Specify the queue
    public schema register(@Payload schema schema,SimpMessageHeaderAccessor headerAccessor){ 
/*
so the above line is bassically to register the user to that channel with our already defined schema 
and to acess the user we use SimpMessageHeaderAccessor and why did we use @payload is The payload may be passed 
through a MessageConverter to convert it from serialized form with a specific MIME type
 to an Object matching the target method parameter .... PS i google it .
*/
        headerAccessor.getSessionAttributes().put("Channel",schema.getUser());
        return schema; 
/* so now we have to get the session attributes then add the 
user name to channel and get it back from the request body and returning the schema 
*/

    }

    @MessageMapping("/chat.send") // Used Map the url from client and server
    @SendTo("/channel/public") // Used to Specify the queue
    public schema sendmessage(@Payload schema Schema){
        return Schema;

    /*  Just this schema basically allows us to send messages 
    */
    }

   

    }


    

