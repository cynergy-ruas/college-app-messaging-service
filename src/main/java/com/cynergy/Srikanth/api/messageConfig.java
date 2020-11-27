package com.cynergy.Srikanth.api; 

import org.springframework.context.annotation.Configuration;  // Used for configration 
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker; // Used to enable Websockets broker
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer; // Used to configurer message broker
import org.springframework.web.socket.config.annotation.StompEndpointRegistry; // Used to Register our STOMP endpoint
import org.springframework.messaging.simp.config.MessageBrokerRegistry; // Used to Register our message endpoint

@Configuration
@EnableWebSocketMessageBroker  
public class messageConfig implements WebSocketMessageBrokerConfigurer {
/*
we are configuring websockets using websocketsconfig class which implements to brokerconfigurer 
basically what brokerconfigurer does is that it allows us to configure message handling 
with messaging protocols in our case we are using STOMP protocol for our websockets.
*/

@Override 
public void registerStompEndpoints(StompEndpointRegistry registry){ 
    // So basically we are registring a STOMP endpoint using registry 
    registry.addEndpoint("/message").withSockJS(); 
    /* So our end point is "/message" where we can send messages using this endpoint 
      as of now we didn't run it with the frontend but this endpoint works and  
     you see that withsockJS() right ? so what that does is it also allows us to connect with HTTP connection */ 
}
    
@Override 
 public void configureMessageBroker(MessageBrokerRegistry registry) { 
     /* So now that we have configured our STOMP endpoint now we have to register our message broker 
     so this is where we configure our message broker using MessageBrokerRegistry using registry */
    registry.enableSimpleBroker("/channel"); /* So this is the message broker's endpoint */
    registry.setApplicationDestinationPrefixes("/allmessage"); // and this is to fetchs all the chat from a channel
}
    
}
