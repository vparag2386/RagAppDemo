package com.example.userproductapp.product;

import com.example.userproductapp.exception.ResourceNotFoundException;
import com.example.userproductapp.product.dto.ProductDTO;
import com.example.userproductapp.product.dto.ProductRequest;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProductService {

    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    public List<ProductDTO> findAll() {
        return productRepository.findAll().stream()
                .map(p -> new ProductDTO(p.getId(), p.getName(), p.getPrice(), p.getDescription()))
                .collect(Collectors.toList());
    }

    public ProductDTO findById(Long id) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found"));
        return new ProductDTO(product.getId(), product.getName(), product.getPrice(), product.getDescription());
    }

    public ProductDTO create(ProductRequest request) {
        Product product = new Product();
        product.setName(request.getName());
        product.setPrice(request.getPrice());
        product.setDescription(request.getDescription());
        Product saved = productRepository.save(product);
        return new ProductDTO(saved.getId(), saved.getName(), saved.getPrice(), saved.getDescription());
    }
}
