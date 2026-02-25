---
name: dart-melos-clean-arch
description: Excellent and idiomatic Dart and Melos workspace management with complex and precise import and dependency control for clean architecture. Use when setting up or managing Dart projects with Melos monorepos, clean architecture layers (domain, data, presentation), dependency injection, and proper import/export patterns across packages.
---

# Dart Melos Clean Architecture Skill

This skill provides workflows for setting up and managing Dart projects using Melos for monorepo management, with a focus on clean architecture principles, precise dependency control, and idiomatic import patterns.

## Clean Architecture Overview

Clean architecture divides the application into layers:
- **Domain**: Business logic, entities, use cases
- **Data**: Data sources, repositories, models
- **Presentation**: UI, controllers, views

Dependencies flow inward: Presentation -> Domain <- Data

## Melos Workspace Setup

1. Initialize Melos in your project root:
   ```bash
   melos init
   ```

2. Configure `pubspec.yaml` for your packages, adding melos dependency and configuration:
   ```yaml
   name: my_melos_workspace
   version: 1.0.0

   dependencies:
     melos: ^7.4.0

   workspace:
     - packages/core

   melos:
     packages:
       - packages/*
   ```

3. Bootstrap the workspace:
   ```bash
   melos bootstrap
   ```

## Package Structure

Organize packages by feature or layer:
- `packages/core` - Shared utilities and abstractions
- `packages/domain` - Business entities and use cases
- `packages/data` - Data layer implementations
- `packages/presentation` - UI packages
- `packages/app` - Main application package and facade
- `packages/datasource_yaml` - Data source implementations using YAML files
- `packages/datasource_rdf` - Data source implementations using RDF files
- `packages/datasource_sembast` - Data source implementations using sembast
- `packages/datasource_hive` - Data source implementations using hive   
- `packages/datasource_config` - Data source implementations using config files
- `packages/datasource_api` - Data source implementations using APIs
- `packages/datasource_sqlite` - Data source implementations using sqlite
- `packages/datasource_shared_preferences` - Data source implementations using shared preferences
- `packages/datasource_firebase` - Data source implementations using firebase
- `packages/datasource_mongodb` - Data source implementations using mongodb
- `packages/datasource_postgresql` - Data source implementations using postgresql
- `packages/datasource_mysql` - Data source implementations using mysql
- `packages/datasource_redis` - Data source implementations using redis
- `packages/datasource_graphql` - Data source implementations using graphql
- `packages/datasource_rest` - Data source implementations using REST APIs
- `packages/datasource_grpc` - Data source implementations using gRPC
- `packages/datasource_websocket` - Data source implementations using WebSockets
- `packages/datasource_amqp` - Data source implementations using AMQP
- `packages/datasource_kafka` - Data source implementations using Kafka
- `packages/datasource_rabbitmq` - Data source implementations using RabbitMQ
- `packages/datasource_cassandra` - Data source implementations using Cassandra
- `packages/datasource_elasticsearch` - Data source implementations using Elasticsearch
- `packages/datasource_influxdb` - Data source implementations using InfluxDB
- `packages/datasource_redis` - Data source implementations using Redis
- `packages/datasource_memcached` - Data source implementations using Memcached
- `packages/datasource_couchdb` - Data source implementations using CouchDB
- `packages/datasource_neo4j` - Data source implementations using Neo4j
- `packages/datasource_oracle` - Data source implementations using Oracle
- `packages/datasource_sqlserver` - Data source implementations using SQL Server
- `packages/datasource_dynamodb` - Data source implementations using DynamoDB
- `packages/datasource_firestore` - Data source implementations using Firestore
- `packages/datasource_supabase` - Data source implementations using Supabase
- `packages/datasource_prisma` - Data source implementations using Prisma
- `packages/datasource_apache_cassandra` - Data source implementations using Apache Cassandra
- `packages/datasource_apache_hadoop` - Data source implementations using Apache Hadoop
- `packages/datasource_apache_spark` - Data source implementations using Apache Spark
- `packages/datasource_apache_kafka` - Data source implementations using Apache Kafka
- `packages/datasource_apache_rabbitmq` - Data source implementations using Apache RabbitMQ
- `packages/datasource_apache_mongodb` - Data source implementations using Apache MongoDB
- `packages/datasource_apache_couchdb` - Data source implementations using Apache CouchDB
- `packages/datasource_apache_neo4j` - Data source implementations using Apache Neo4j
- `packages/datasource_apache_oracle` - Data source implementations using Apache Oracle
- `packages/datasource_apache_sqlserver` - Data source implementations using Apache SQL Server
- `packages/datasource_apache_dynamodb` - Data source implementations using Apache DynamoDB
- `packages/datasource_apache_firestore` - Data source implementations using Apache Firestore
- `packages/datasource_apache_supabase` - Data source implementations using Apache Supabase
- `packages/datasource_apache_prisma` - Data source implementations using Apache Prisma
- `packages/datasource_apache_cassandra` - Data source implementations using Apache Cassandra
- `packages/datasource_apache_hadoop` - Data source implementations using Apache Hadoop
- `packages/datasource_apache_spark` - Data source implementations using Apache Spark
- `packages/datasource_apache_kafka` - Data source implementations using Apache Kafka
- `packages/datasource_apache_rabbitmq` - Data source implementations using Apache RabbitMQ
- `packages/datasource_apache_mongodb` - Data source implementations using Apache Mongo

## Dependency Management

Use Melos to manage dependencies across packages:
- Define shared dependencies in root `pubspec.yaml`
- Use path dependencies for local packages
- Keep external dependencies minimal and version-pinned

## Import Patterns

- Use relative imports within packages
- Export public APIs from `lib/<package>.dart`
- Avoid circular dependencies

## References

- [Clean Architecture Guidelines](references/clean-architecture.md)

## Assets

- `assets/dart_package_template/pubspec.yaml` - Sample melos package configuration
- `assets/flutter_package_template/pubspec.yaml` - Sample Flutter package configuration