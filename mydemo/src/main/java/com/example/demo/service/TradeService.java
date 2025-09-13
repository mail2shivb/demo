package com.example.demo.service;

import com.example.demo.entity.Trade;
import com.example.demo.repository.TradeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TradeService {
    @Autowired
    private TradeRepository tradeRepository;

    public List<Trade> getAllTrades() {
        return tradeRepository.findAll();
    }

    public Optional<Trade> getTradeById(Long id) {
        return tradeRepository.findById(id);
    }

    public Trade createTrade(Trade trade) {
        return tradeRepository.save(trade);
    }

    public Trade updateTrade(Long id, Trade tradeDetails) {
        return tradeRepository.findById(id)
                .map(trade -> {
                    trade.setSymbol(tradeDetails.getSymbol());
                    trade.setQuantity(tradeDetails.getQuantity());
                    trade.setPrice(tradeDetails.getPrice());
                    return tradeRepository.save(trade);
                })
                .orElse(null);
    }

    public boolean deleteTrade(Long id) {
        return tradeRepository.findById(id)
                .map(trade -> {
                    tradeRepository.delete(trade);
                    return true;
                })
                .orElse(false);
    }
}
