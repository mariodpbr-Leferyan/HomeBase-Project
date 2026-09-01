# Data Model — HomeBase

This document describes the main entities (tables) and how they relate to each other. We'll build them progressively, phase by phase — this document gets updated as we go.

## Central entity: Household

Everything revolves around the **Household** concept. It's what allows multiple users to share the same data.

```
Household
├── id
├── name              (e.g. "Silva Family")
└── created_at

User
├── id
├── household_id      (which household it belongs to)
├── name
├── email
├── password_hash      (never the plain-text password!)
├── role                (e.g. "admin", "member")
└── created_at
```

## Phase 2 — Invoice

```
Invoice
├── id
├── household_id
├── created_by (user_id)
├── amount
├── issue_date
├── category          (e.g. electricity, water, internet)
├── status            (registered / paid)
└── created_at
```

## Phase 3 — Expense (Food)

```
Expense
├── id
├── household_id
├── created_by
├── amount
├── category          (e.g. food, transport, leisure)
├── date
├── description
└── created_at
```

## Phase 4 — RecurringPayment

```
RecurringPayment
├── id
├── household_id
├── name              (e.g. "Rent", "Netflix")
├── amount
├── frequency          (monthly / yearly / weekly)
├── due_day            (day of month/week it's due)
├── status             (pending / paid / overdue)
└── last_paid_at
```

## Phase 5 — Budget

```
Budget
├── id
├── household_id
├── category
├── limit_amount
├── period             (e.g. "2026-09")
```

## Phase 6 — Event (Calendar)

```
Event
├── id
├── household_id
├── created_by
├── title
├── type               (activity / task / appointment)
├── start_datetime
├── end_datetime
└── notes
```

## Phase 7 — ShoppingList / ShoppingItem

```
ShoppingList
├── id
├── household_id
└── name

ShoppingItem
├── id
├── shopping_list_id
├── name
├── quantity
├── is_bought          (true/false)
└── added_by
```

## Phase 8 — WishlistItem

```
WishlistItem
├── id
├── household_id
├── name
├── url                (direct link to the store)
├── store               (e.g. "Amazon", "Fnac")
├── estimated_price
├── priority            (low / medium / high)
└── added_by
```

## Relationship summary

- One **Household** has many **Users**.
- One **Household** has many **Invoices**, **Expenses**, **RecurringPayments**, **Budgets**, **Events**, **ShoppingLists**, and **WishlistItems**.
- This is called a **"one-to-many"** relationship — you'll see this pattern repeat across almost every model, which makes learning much easier: once you understand one, you understand nearly all of them.

## Simplified diagram

```
Household ──┬── Users
            ├── Invoices
            ├── Expenses
            ├── RecurringPayments
            ├── Budgets
            ├── Events
            ├── ShoppingLists ── ShoppingItems
            └── WishlistItems
```
