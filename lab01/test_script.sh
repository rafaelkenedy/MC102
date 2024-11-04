#!/bin/bash

input_file="test.in"
output_file="test.out"
expected_output_file="expected.out"

python3 lab01.py < "$input_file" > "$output_file"

if diff "$output_file" "$expected_output_file" > /dev/null; then
    echo "Teste passou"
else
    echo "Teste falhou"
    echo "Saída gerada:"
    cat "$output_file"
    echo ""
    echo "Saída esperada:"
    cat "$expected_output_file"
fi
