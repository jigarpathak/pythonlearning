//src/main/java/com/example/model

package com.example.model;

import com.azure.spring.data.cosmos.core.mapping.Container;
import org.springframework.data.annotation.Id;

@Container(containerName = "Products")
public class Product {

    @Id
    private String id;
    private String name;
    private String category;
    private double price;

    // Constructors, Getters, and Setters
}
