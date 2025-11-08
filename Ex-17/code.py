def cortar_barra_topdown(precios, n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, precios[i - 1] + cortar_barra_topdown(precios, n - i, memo))
    
    memo[n] = max_val
    return max_val

def cortar_barra_topdown_sol(precios, n, memo=None, cortes_memo=None):
    if memo is None:
        memo = {}
        cortes_memo = {}
    if n == 0:
        return 0, []
    if n in memo:
        return memo[n], cortes_memo[n]
    
    max_val = float('-inf')
    mejor_corte = []
    
    for i in range(1, n + 1):
        valor, cortes = cortar_barra_topdown_sol(precios, n - i, memo, cortes_memo)
        valor_total = precios[i - 1] + valor
        if valor_total > max_val:
            max_val = valor_total
            mejor_corte = [i] + cortes
    
    memo[n] = max_val
    cortes_memo[n] = mejor_corte
    return max_val, mejor_corte

def cortar_barra_bottomup(precios, n):
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, precios[j - 1] + dp[i - j])
        dp[i] = max_val
    
    return dp[n]

def cortar_barra_bottomup_sol(precios, n):
    dp = [0] * (n + 1)
    cortes = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = float('-inf')
        mejor_corte = 0
        for j in range(1, i + 1):
            if precios[j - 1] + dp[i - j] > max_val:
                max_val = precios[j - 1] + dp[i - j]
                mejor_corte = j
        dp[i] = max_val
        cortes[i] = mejor_corte
    
    # reconstruir la solución óptima
    res = []
    longitud = n
    while longitud > 0:
        res.append(cortes[longitud])
        longitud -= cortes[longitud]
    
    return dp[n], res


precios = [1, 5, 8, 9]  # p1=1, p2=5, p3=8, p4=9
n = 4

print(cortar_barra_topdown(precios, n))               # 10
print(cortar_barra_topdown_sol(precios, n))           # (10, [2, 2])

print(cortar_barra_bottomup(precios, n))              # 10
print(cortar_barra_bottomup_sol(precios, n))          # (10, [2, 2])
