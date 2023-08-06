package com.ai.conroller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.ai.dto.ChatRequest;
import com.ai.dto.ChatResponse;

@RestController
@RequestMapping("/main")
@CrossOrigin("*")
public class MainController {
	
	@Value("${openai.api.url}")
	private String url;
	
	@Value("${openai.api.model}")
	private String model;
	
	
	@Value("${openai.api.key}")
	private String token;
	
	private RestTemplate resTemp;
	
 	@Autowired
	public void setResTemp(RestTemplate resTemp) {
		this.resTemp = resTemp;
	}



	@PostMapping("/chat")
	public  ResponseEntity<ChatResponse> getResponse(@RequestParam("prompt") String prompt){
		
		HttpHeaders headers = new HttpHeaders();
		headers.add("Authorization", "Bearer " +token);
		
		
		
		ChatRequest request= new ChatRequest(model,prompt);
		
		
		HttpEntity<ChatRequest> http = new HttpEntity<>(request, headers);
		
		
		ResponseEntity<ChatResponse> res= resTemp.exchange(url, HttpMethod.POST, http, ChatResponse.class);
		
		ChatResponse ob= res.getBody();
//		List<Choice> list= ob.getChoices();
//		for(Choice ch:list) {
//			System.out.println(ch.getIndex()+" "+ch.getMessage());
//		}
		return new ResponseEntity<>(ob,HttpStatus.ACCEPTED);
	} 
	
	
	
	
}
