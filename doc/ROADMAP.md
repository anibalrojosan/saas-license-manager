## 🚀 Project Roadmap

This project follows a feature-branch workflow. Each phase corresponds to a specific branch and set of requirements.

### Phase 1: Project Foundation 🏗️
**Branch:** `feature/project-setup`
- [x] Initialize Git repository.
- [x] Create project structure (folders & `__init__.py` files).
- [x] Add `.gitignore`, `README.md`, and `doc/classdiagram`.
- [x] Define the base `License` class in `core/models.py`.

### Phase 2: Core Logic & Data Structures 🧠
**Branch:** `feature/core-logic`
- [ ] Implement `LicenseManager` class in `core/manager.py`.
- [ ] Set up the main list to store license objects.
- [ ] Implement a **Set** to manage unique software providers.
- [ ] Create the `to_dict()` method for data manipulation.

### Phase 3: CRUD Operations 🛠️
**Branch:** `feature/license-crud`
- [ ] **Create**: Add functionality to input new licenses.
- [ ] **Read**: Display all licenses in a formatted table.
- [ ] **Update**: Modify existing license details.
- [ ] **Delete**: Remove licenses by ID.

### Phase 4: Business Logic & Reports 📊
**Branch:** `feature/reporting`
- [ ] Implement total monthly cost calculation.
- [ ] Add filtering capabilities (e.g., search by provider).
- [ ] Create a summary report of all active subscriptions.

### Phase 5: User Interface & Validation 🖥️
**Branch:** `feature/ui-ux`
- [ ] Build the main menu loop in `main.py`.
- [ ] Implement robust input validation (prevent empty strings or invalid prices).
- [ ] Add error handling (`try/except`) for user inputs.

### Phase 6: Final Review & PEP 8
**Branch:** `feature/final-review`
- [ ] Final code refactoring.
- [ ] Ensure full compliance with **PEP 8** standards.
- [ ] Complete documentation and final testing.