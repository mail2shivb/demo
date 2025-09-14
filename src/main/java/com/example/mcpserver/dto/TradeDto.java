package com.example.mcpserver.dto;

import java.time.Instant;

public record TradeDto(
        Long id,
        String symbol,
        int quantity,
        double price,
        Instant executedAt) {
}
