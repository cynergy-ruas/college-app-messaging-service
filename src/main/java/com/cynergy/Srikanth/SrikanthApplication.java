package com.cynergy.Srikanth;

import com.cynergy.Srikanth.db.messagerepo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication; 
import org.springframework.boot.autoconfigure.SpringBootApplication;



@SpringBootApplication
public class SrikanthApplication {

@Autowired
private static messagerepo messagerepo;  // Declaring the class 

public static void main(String[] args) {
	SpringApplication.run(SrikanthApplication.class, args);
	System.out.println(messagerepo.findAll());
		

	/* Basic Run Function and still having a error while running it the 
	data is null can you please help me out and thanks :) 
	sorry if my commenting was bad */
	}
}
