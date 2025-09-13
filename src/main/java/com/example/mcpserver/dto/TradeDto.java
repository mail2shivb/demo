package com.example.mcpserver.dto;

public record TradeDto(
        Long id,
        String symbol,
        int quantity,
        double price) {
}
