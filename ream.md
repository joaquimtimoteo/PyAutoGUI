# Expressões regulares (ou *regex*, de *regular expressions*) são sequências de caracteres que formam um padrão de busca. São amplamente utilizadas para procurar e manipular texto em linguagens de programação e ferramentas de processamento de texto. Esses padrões podem ser usados para verificar se uma determinada sequência de caracteres está presente em um texto, extrair partes específicas, substituir substrings, validar formatos, entre outras tarefas.

![alt text](image.png)

# Aqui estão alguns exemplos do que é possível fazer com expressões regulares:

- **Verificar formatos**: Validar se uma entrada de usuário segue um padrão específico, como um email (`^\w+@\w+\.\w+$`), número de telefone ou CPF.
- **Procurar e substituir**: Localizar todas as ocorrências de uma palavra em um texto e substituí-las por outra.
- **Extração de informações**: Extrair dados específicos, como endereços de email em um texto ou números em uma página da web.

### Sintaxe básica de expressões regulares
Alguns elementos comuns em regex incluem:
- `.`: Representa qualquer caractere, exceto uma nova linha.
- `*`: Indica que o caractere anterior pode aparecer zero ou mais vezes.
- `+`: Indica que o caractere anterior deve aparecer uma ou mais vezes.
- `?`: Torna o caractere anterior opcional.
- `\d`: Representa um dígito (0-9).
- `\w`: Representa qualquer caractere alfanumérico (letras e números).
- `[]`: Define uma classe de caracteres, permitindo combinar vários caracteres, por exemplo, `[abc]` combina "a", "b" ou "c".

### Exemplos práticos
1. **Validação de email**: `^\w+@\w+\.\w+$`
2. **Extrair números**: `\d+`
3. **Telefone (exemplo simples)**: `^\(\d{2}\) \d{4,5}-\d{4}$` para números no formato "(XX) XXXXX-XXXX".

As expressões regulares podem variar um pouco entre linguagens, mas a maioria segue essa estrutura básica.