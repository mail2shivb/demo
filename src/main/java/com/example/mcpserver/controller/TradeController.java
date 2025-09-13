package com.example.mcpserver.controller;

import com.example.mcpserver.entity.Trade;
import com.example.mcpserver.service.TradeMcpService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/trades")
public class TradeController {
    @Autowired
    private TradeMcpService tradeMcpService;

    @GetMapping
    public List<Trade> getAllTrades() {
        return tradeMcpService.getAllTrades();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Trade> getTradeById(@PathVariable Long id) {
        Optional<Trade> trade = tradeMcpService.getTradeById(id);
        return trade.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public Trade createTrade(@RequestBody Trade trade) {
        return tradeMcpService.createTrade(trade);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Trade> updateTrade(@PathVariable Long id, @RequestBody Trade tradeDetails) {
        Trade updatedTrade = tradeMcpService.updateTrade(id, tradeDetails);
        if (updatedTrade != null) {
            return ResponseEntity.ok(updatedTrade);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteTrade(@PathVariable Long id) {
        boolean deleted = tradeMcpService.deleteTrade(id);
        if (deleted) {
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
