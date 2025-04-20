from django.shortcuts import render,HttpResponse
# Create your views here.

def home(request):
    """Render the home page."""
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-sky-100 to-indigo-200 min-h-screen flex items-center justify-center px-4">

  <div class="bg-white/80 shadow-xl rounded-xl max-w-xl w-full p-8 text-center backdrop-blur-md">
    
    <h1 class="text-3xl font-bold text-indigo-700 mb-4">Bem-vindo à Página Inicial! 👋</h1>
    
    <p class="text-gray-700 mb-2">Esta é a página inicial do seu site.</p>
    <p class="text-gray-600 mb-2">Você pode adicionar mais conteúdo aqui.</p>
    <p class="text-gray-600 mb-6">Se precisar de ajuda, entre em contato conosco.</p>
    
    <div class="flex flex-col gap-4">
      <a href="/ramais/" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 rounded-md transition-all duration-200">
        Lista de Ramais
      </a>
      <a href="/pinterest/login/" class="bg-pink-500 hover:bg-pink-600 text-white font-semibold py-2 rounded-md transition-all duration-200">
        Pinterest
      </a>
      <a href="/adote/usuario/logar/" class="bg-green-500 hover:bg-green-600 text-white font-semibold py-2 rounded-md transition-all duration-200">
        Adote
      </a>
    </div>

  </div>

</body>
</html>

    """)