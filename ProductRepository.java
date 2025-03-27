//src/main/java/com/example/repository
package com.example.repository;

import com.example.model.Product;
import com.azure.spring.data.cosmos.repository.CosmosRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends CosmosRepository<Product, String> {
}
