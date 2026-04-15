#!/usr/bin/env python3
"""
Simulation script for printing Xendit mutation history.
This uses dummy data to simulate transaction mutations.
"""

import datetime
import random

def generate_dummy_mutations():
    """Generate a list of dummy mutation records."""
    mutations = [
        {
            "date": "2024-04-10",
            "time": "14:30:00",
            "amount": 50000,
            "type": "credit",
            "description": "Payment received from customer ABC",
            "reference": "TXN-001234"
        },
        {
            "date": "2024-04-09",
            "time": "09:15:00",
            "amount": -25000,
            "type": "debit",
            "description": "Transfer to supplier XYZ",
            "reference": "TXN-001235"
        },
        {
            "date": "2024-04-08",
            "time": "16:45:00",
            "amount": 75000,
            "type": "credit",
            "description": "Refund processed",
            "reference": "TXN-001236"
        },
        {
            "date": "2024-04-07",
            "time": "11:20:00",
            "amount": -15000,
            "type": "debit",
            "description": "Service fee deduction",
            "reference": "TXN-001237"
        },
        {
            "date": "2024-04-06",
            "time": "13:10:00",
            "amount": 100000,
            "type": "credit",
            "description": "Bulk payment received",
            "reference": "TXN-001238"
        }
    ]
    return mutations

def format_currency(amount):
    """Format amount as currency string."""
    return f"Rp {abs(amount):,}".replace(",", ".")

def print_mutation_history(mutations):
    """Print the mutation history in a formatted table."""
    print("Xendit Mutation History Simulation")
    print("=" * 80)
    print(f"{'Date':<12} {'Time':<10} {'Type':<8} {'Amount':<15} {'Description':<30} {'Reference'}")
    print("-" * 80)

    for mutation in mutations:
        amount_str = format_currency(mutation["amount"])
        if mutation["type"] == "debit":
            amount_str = f"-{amount_str}"

        print(f"{mutation['date']:<12} {mutation['time']:<10} {mutation['type']:<8} {amount_str:<15} {mutation['description']:<30} {mutation['reference']}")

    print("-" * 80)

    # Calculate totals
    total_credits = sum(m["amount"] for m in mutations if m["type"] == "credit")
    total_debits = sum(abs(m["amount"]) for m in mutations if m["type"] == "debit")
    net_balance = total_credits - total_debits

    print(f"Total Credits: {format_currency(total_credits)}")
    print(f"Total Debits:  {format_currency(total_debits)}")
    print(f"Net Balance:   {format_currency(net_balance)}")

def main():
    """Main function to run the simulation."""
    print("Simulating Xendit mutation history retrieval...")
    print()

    # Simulate API delay
    import time
    time.sleep(1)

    mutations = generate_dummy_mutations()
    print_mutation_history(mutations)

if __name__ == "__main__":
    main()
