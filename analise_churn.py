import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar a base de dados
df = pd.read_excel('clientes_ecommerce.xlsx')

# 2. Calcular o prejuízo por status de Churn
faturamento_status = df.groupby('Churn')['Valor_Mensal'].sum().reset_index()
faturamento_status['Churn'] = faturamento_status['Churn'].map({'Nao': 'Clientes Ativos', 'Sim': 'Prejuízo (Churn)'})

# 3. Configurar o visual do gráfico
plt.figure(figsize=(8, 6))
sns.set_theme(style="whitegrid")

grafico = sns.barplot(
    x='Churn', 
    y='Valor_Mensal', 
    data=faturamento_status, 
    palette=['#2ecc71', '#e74c3c']
)

plt.title('Impacto Financeiro Mensal: Retenção vs Cancelamento', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Status do Cliente', fontsize=12)
plt.ylabel('Receita Recorrente Mensal (R$)', fontsize=12)

for p in grafico.patches:
    grafico.annotate(
        f"R$ {p.get_height():,.2f}",
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center',
        xytext=(0, 9),
        textcoords='offset points',
        fontsize=11, fontweight='bold'
    )

plt.tight_layout()

# 🔥 Salva o gráfico direto como uma imagem na sua pasta (sem abrir janela para travar!)
plt.savefig('grafico_impacto_financeiro.png', dpi=300)
print("Sucesso! O gráfico foi gerado e salvo como a imagem 'grafico_impacto_financeiro.png' na sua pasta!")