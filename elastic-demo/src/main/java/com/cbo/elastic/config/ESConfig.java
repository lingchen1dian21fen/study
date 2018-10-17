package com.cbo.elastic.config;

import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.transport.client.PreBuiltTransportClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * Created by corning on 2018/3/5.
 */
@Configuration
public class ESConfig {

    @Bean
    public TransportClient client() throws UnknownHostException {

        Settings settings = Settings.builder().put("cluster.name", "test_es").build();

        PreBuiltTransportClient client = new PreBuiltTransportClient(settings);

        client.addTransportAddress(new InetSocketTransportAddress(
        		InetAddress.getByName("192.168.252.129"), 9300));
        
        client.addTransportAddress(new InetSocketTransportAddress(
        		InetAddress.getByName("192.168.252.131"), 9300));
        return client;

    }

}
