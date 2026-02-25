# Clean Architecture Guidelines for Dart

## Principles

1. **Dependency Inversion**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

2. **Single Responsibility**: Each class should have only one reason to change.

3. **Open/Closed**: Entities should be open for extension but closed for modification.

## Layer Responsibilities

### Domain Layer Packages

#### Entities Package

- Entities: Business objects

#### Usecases Package

- Use Cases: Application-specific business rules

#### Contracts Packages

- Repositories: Abstract data interfaces for repositories (persisted entities), or services.

### Data Layer Package(s), usually by tech or feature

- Models: Data transfer objects
- Data Sources: External data access (API, DB)
- Repositories: Concrete implementations

### Presentation Package including wiring and facade

- Views: UI components
- Controllers: UI logic and state management
- Presenters: Format data for display

## Dependency Flow

NB, we break our domain up into three packages to ensure crisp dependencies.
Some datasources use usecases, others contracts, others both.
They'll get access to the entities through those packages.

```
CLI or Flutter
     ↓
App/Facade Package
     ↓
Datasource Package(s)
     ↓
Usecases Package
     ↓
Contracts Package
     ↓
Entities Package
```
