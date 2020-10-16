package com.cynergy.Srikanth.api;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;

@Configuration
@EnableWebSocketMessageBroker
public class websocketsconfig implements WebSocketMessageBrokerConfigurer {

@Override 
public void registerStompEndpoints(StompEndpointRegistry registry){ // To register STOMP endpoint
    registry.addEndpoint("/message").withSockJS();  // Adding end point with HTTP connection option 


}
    
@Override 
 public void configureMessageBroker(MessageBrokerRegistry registry) { // This to configure message broker
    registry.enableSimpleBroker("/channel");  //Broker endpoint
    registry.setApplicationDestinationPrefixes("/allmessage"); //appliation endpoint 
}
    

}
