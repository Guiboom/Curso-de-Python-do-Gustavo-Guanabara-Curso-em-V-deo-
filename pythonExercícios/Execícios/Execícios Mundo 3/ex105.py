def notas(*nums, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    
    :param nums: Uma ou mais notas dos alunos (aceita múltiplas notas).
    :param sit: (Opcional) Indica se deve ou não adicionar a situação da média no dicionário.
    :return: Dicionário com o total de notas, a maior, a menor, a média e a situação (se solicitada).
    """
    
    dictnotas = {
        "total": len(nums),
        "maior": max(nums),
        "menor": min(nums),
        "media": sum(nums) / len(nums)
    }

    if sit == True:
        media = sum(nums) / len(nums)
        if media < 6:
            dictnotas["situção"] = "RUIM"
        elif media < 7:
            dictnotas["situção"] = "RAZOAVEL"
        elif media >= 7:
            dictnotas["situção"] = "BOA"

    return dictnotas

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)