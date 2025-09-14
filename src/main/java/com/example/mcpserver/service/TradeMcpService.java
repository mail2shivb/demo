package com.example.mcpserver.service;

import com.example.mcpserver.entity.Trade;
import com.example.mcpserver.repository.TradeRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.ai.tool.annotation.Tool;
import org.springframework.ai.tool.annotation.ToolParam;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class TradeMcpService {
    private final TradeRepository tradeRepository;

    @Tool(name = "getAllTrades", description = "Retrieve all trades from the repository")
    public List<Trade> getAllTrades() {
        return tradeRepository.findAll();
    }

    @Tool(name = "getTradeById", description = "Retrieve a trade by its ID")
    public Optional<Trade> getTradeById(@ToolParam Long id) {
        return tradeRepository.findById(id);
    }

    @Tool(name = "createTrade", description = "Create a new trade")
    public Trade createTrade(@ToolParam Trade trade) {
        return tradeRepository.save(trade);
    }

    @Tool(name = "updateTrade", description = "Update an existing trade by ID")
    public Trade updateTrade(
            @ToolParam Long id,
            @ToolParam Trade tradeDetails) {
        return tradeRepository.findById(id)
                .map(trade -> {
                    trade.setSymbol(tradeDetails.getSymbol());
                    trade.setQuantity(tradeDetails.getQuantity());
                    trade.setPrice(tradeDetails.getPrice());
                    trade.setExecutedAt(tradeDetails.getExecutedAt());
                    return tradeRepository.save(trade);
                })
                .orElse(null);
    }

    @Tool(name = "deleteTrade", description = "Delete a trade by its ID")
    public boolean deleteTrade(@ToolParam Long id) {
        return tradeRepository.findById(id)
                .map(trade -> {
                    tradeRepository.delete(trade);
                    return true;
                })
                .orElse(false);
    }
}
