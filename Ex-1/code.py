s = "aquestaesunafrasequepodiaserunexemple"
D = {"aquesta", "es", "una", "frase", "que", "podia", "ser", "un", "exemple"}

def existe_segmentacion_topdown(s, D, i=0, memo=None):
    """
    Verifica si la cadena s puede ser segmentada en palabras del diccionario D
    comenzando desde el índice i utilizando memoización. Es la versión top-down
    """
    if memo is None:
        memo = {}
    if i == len(s):
        return True
    if i in memo:
        return memo[i]
    
    for j in range(i + 1, len(s) + 1):
        palabra = s[i:j]
        if palabra in D and existe_segmentacion_topdown(s, D, j, memo):
            memo[i] = True
            return True
    memo[i] = False
    return False

def reconstruir_frase_topdown(s, D, i=0, memo=None):
    """
    Reconstruye una frase segmentada de la cadena s utilizando palabras del
    diccionario D comenzando desde el índice i utilizando memoización. Es la
    versión top-down
    """
    if memo is None:
        memo = {}
    if i == len(s):
        return ""
    if i in memo:
        return memo[i]
    
    for j in range(i + 1, len(s) + 1):
        palabra = s[i:j]
        if palabra in D:
            resto = reconstruir_frase_topdown(s, D, j, memo)
            if resto is not None:
                if resto == "":
                    memo[i] = palabra
                else:
                    memo[i] = palabra + " " + resto
                return memo[i]
    memo[i] = None
    return None

def existe_segmentacion_bottomup(s, D):
    """
    Verifica si la cadena s puede ser segmentada en palabras del diccionario D
    utilizando programación dinámica bottom-up.
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # cadena vacía = válida
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in D:
                dp[i] = True
                break
    return dp[n]

def reconstruir_frase_bottomup(s, D):
    """
    Reconstruye una frase segmentada de la cadena s utilizando palabras del
    diccionario D utilizando programación dinámica bottom-up.
    """
    n = len(s)
    dp = [False] * (n + 1)
    prev = [-1] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in D:
                dp[i] = True
                prev[i] = j
                break
    
    if not dp[n]:
        return None
    
    # reconstruir frase hacia atrás
    palabras = []
    i = n
    while i > 0:
        j = prev[i]
        palabras.append(s[j:i])
        i = j
    palabras.reverse()
    return " ".join(palabras)


print(existe_segmentacion_topdown(s, D))      # True
print(reconstruir_frase_topdown(s, D))        # "aquesta es una frase que podia ser un exemple"

print(existe_segmentacion_bottomup(s, D))     # True
print(reconstruir_frase_bottomup(s, D))       # "aquesta es una frase que podia ser un exemple"
