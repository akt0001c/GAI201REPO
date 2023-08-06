package com.ai.exceptions;

import java.time.LocalDateTime;

import lombok.Data;

@Data
public class ErrorDetails {
 private LocalDateTime timeStamp;
 private String discription;
 private String message;
}
