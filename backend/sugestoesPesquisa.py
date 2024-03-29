import random

sugestoes = [

        {'id': 1, 'pesquisa': 'Dê-me uma ideia de startup para um aplicativo de saúde.', 'assunto': 'Saúde'},
        {'id': 2, 'pesquisa': 'Uma ideia inovadora para um aplicativo de saúde poderia ser...', 'assunto': 'Saúde'},
        {'id': 3, 'pesquisa': 'Isso é interessante, mas gostaria de algo mais focado em tecnologia wearable.',
         'assunto': 'Tecnologia'},
        {'id': 4, 'pesquisa': 'Certamente! Uma startup de tecnologia wearable pode oferecer...',
         'assunto': 'Tecnologia'},
        {'id': 5, 'pesquisa': 'Preciso de uma ideia de startup para a área de sustentabilidade.',
         'assunto': 'Sustentabilidade'},
        {'id': 6, 'pesquisa': 'Uma startup sustentável pode oferecer soluções para...', 'assunto': 'Sustentabilidade'},
        {'id': 7, 'pesquisa': 'Estou interessado em uma ideia de startup relacionada à inteligência artificial.',
         'assunto': 'Inteligência Artificial'},
        {'id': 8, 'pesquisa': 'Uma startup de IA inovadora pode focar em...', 'assunto': 'Inteligência Artificial'},
        {'id': 9, 'pesquisa': 'Quero uma ideia de startup que envolva realidade aumentada.',
         'assunto': 'Realidade Aumentada'},
        {'id': 10, 'pesquisa': 'Uma startup de realidade aumentada pode criar...', 'assunto': 'Realidade Aumentada'},
        {'id': 11, 'pesquisa': 'Estou buscando uma ideia de startup para melhorar a educação online.',
         'assunto': 'Educação'},
        {'id': 12, 'pesquisa': 'Uma startup educacional online inovadora pode fornecer...', 'assunto': 'Educação'},
        {'id': 13, 'pesquisa': 'Como criar uma startup para transformar a experiência de compras online?',
         'assunto': 'Compras Online'},
        {'id': 14, 'pesquisa': 'Uma startup revolucionária de compras online pode oferecer...',
         'assunto': 'Compras Online'},
        {'id': 15, 'pesquisa': 'Quero uma ideia de startup focada em facilitar a comunicação remota.',
         'assunto': 'Comunicação Remota'},
        {'id': 16, 'pesquisa': 'Uma startup de comunicação remota pode desenvolver...', 'assunto': 'Comunicação Remota'},
        {'id': 17, 'pesquisa': 'Gostaria de uma ideia de startup para promover a inclusão social.',
         'assunto': 'Questões Sociais'},
        {'id': 18, 'pesquisa': 'Uma startup focada em inclusão social pode criar soluções para...',
         'assunto': 'Questões Sociais'},
        {'id': 19, 'pesquisa': 'Preciso de uma ideia de startup para aprimorar a gestão de projetos.',
         'assunto': 'Sustentabilidade'},
        {'id': 20, 'pesquisa': 'Uma startup de gestão de projetos inovadora pode introduzir...',
         'assunto': 'Sustentabilidade'},
        {'id': 21, 'pesquisa': 'Quero criar uma startup voltada para o setor de alimentos. Alguma sugestão?',
         'assunto': 'Saúde'},
        {'id': 22, 'pesquisa': 'Uma startup alimentar inovadora pode explorar oportunidades em...', 'assunto': 'Saúde'},
        {'id': 23, 'pesquisa': 'Estou interessado em uma ideia de startup relacionada à Internet das Coisas.',
         'assunto': 'Tecnologia'},
        {'id': 24,
         'pesquisa': 'Uma startup de IoT pode se concentrar em...Preciso de uma ideia de startup para uma solução sustentável de embalagens.',
         'assunto': 'Sustentabilidade'},
        {'id': 25, 'pesquisa': 'Uma startup focada em embalagens sustentáveis pode oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 26, 'pesquisa': 'Gostaria de uma ideia para uma startup no setor de mobilidade urbana.',
         'assunto': 'Mobilidade Urbana'},
        {'id': 27, 'pesquisa': 'Uma ideia inovadora para mobilidade urbana poderia ser...',
         'assunto': 'Mobilidade Urbana'},
        {'id': 28, 'pesquisa': 'Quero uma startup relacionada à educação online para crianças.', 'assunto': 'Educação'},
        {'id': 29, 'pesquisa': 'Uma startup de educação online para crianças pode criar...', 'assunto': 'Educação'},
        {'id': 30, 'pesquisa': 'Estou interessado em uma ideia de startup de tecnologia para o setor agrícola.',
         'assunto': 'Sustentabilidade'},
        {'id': 31, 'pesquisa': 'Uma startup agritech poderia desenvolver...', 'assunto': 'Sustentabilidade'},
        {'id': 32, 'pesquisa': 'Preciso de uma ideia para uma startup de aplicativo de fitness personalizado.',
         'assunto': 'Sustentabilidade'},
        {'id': 33, 'pesquisa': 'Uma startup de fitness personalizado pode oferecer um aplicativo que...',
         'assunto': 'Sustentabilidade'},
        {'id': 34, 'pesquisa': 'Gostaria de uma ideia de startup voltada para o mercado de turismo.',
         'assunto': 'Sustentabilidade'},
        {'id': 35, 'pesquisa': 'Uma startup no setor de turismo pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 36, 'pesquisa': 'Quero uma ideia para uma startup de plataforma de colaboração online.',
         'assunto': 'Sustentabilidade'},
        {'id': 37, 'pesquisa': 'Uma startup de colaboração online pode criar uma plataforma que...',
         'assunto': 'Sustentabilidade'},
        {'id': 38, 'pesquisa': 'Estou pensando em uma startup de soluções para o envelhecimento da população.',
         'assunto': 'Saúde'},
        {'id': 39, 'pesquisa': 'Uma startup focada em soluções para o envelhecimento pode desenvolver...',
         'assunto': 'Saúde'},
        {'id': 40, 'pesquisa': 'Preciso de uma ideia para uma startup de assistência virtual à saúde.',
         'assunto': 'Saúde'},
        {'id': 41, 'pesquisa': 'Uma startup de assistência virtual à saúde poderia oferecer...', 'assunto': 'Saúde'},
        {'id': 42, 'pesquisa': 'Gostaria de uma ideia para uma startup que integre tecnologia e moda.',
         'assunto': 'Sustentabilidade'},
        {'id': 43, 'pesquisa': 'Uma startup que integra tecnologia e moda pode criar...', 'assunto': 'Sustentabilidade'},
        {'id': 44, 'pesquisa': 'Quero uma ideia para uma startup de soluções de pagamento inovadoras.',
         'assunto': 'Sustentabilidade'},
        {'id': 45, 'pesquisa': 'Uma startup de soluções de pagamento inovadoras poderia desenvolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 46, 'pesquisa': 'Estou buscando uma ideia para uma startup de energia renovável.',
         'assunto': 'Energias Renováveis'},
        {'id': 47, 'pesquisa': 'Uma startup de energia renovável pode se destacar ao...',
         'assunto': 'Energias Renováveis'},
        {'id': 48, 'pesquisa': 'Preciso de uma ideia para uma startup de reciclagem de resíduos eletrônicos.',
         'assunto': 'Sustentabilidade'},
        {'id': 49, 'pesquisa': 'Uma startup de reciclagem de resíduos eletrônicos pode...',
         'assunto': 'Sustentabilidade'},
        {'id': 50, 'pesquisa': 'Gostaria de uma ideia para uma startup que promova a inclusão social.',
         'assunto': 'Questões Sociais'},
        {'id': 51, 'pesquisa': 'Uma startup focada em inclusão social pode criar...', 'assunto': 'Questões Sociais'},
        {'id': 52, 'pesquisa': 'Quero uma ideia para uma startup que utilize realidade aumentada.',
         'assunto': 'Realidade Aumentada'},
        {'id': 53, 'pesquisa': 'Uma startup que utiliza realidade aumentada pode desenvolver...',
         'assunto': 'Realidade Aumentada'},
        {'id': 54, 'pesquisa': 'Estou interessado em uma ideia de startup no setor de entretenimento digital.',
         'assunto': 'Sustentabilidade'},
        {'id': 55, 'pesquisa': 'Uma startup de entretenimento digital pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 56, 'pesquisa': 'Preciso de uma ideia para uma startup de delivery de produtos orgânicos.',
         'assunto': 'Sustentabilidade'},
        {'id': 57, 'pesquisa': 'Uma startup de delivery de produtos orgânicos poderia oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 58, 'pesquisa': 'Gostaria de uma ideia para uma startup de soluções de saúde mental.',
         'assunto': 'Saúde'},
        {'id': 59, 'pesquisa': 'Uma startup de soluções de saúde mental pode criar...', 'assunto': 'Saúde'},
        {'id': 60, 'pesquisa': 'Quero uma ideia para uma startup de tecnologia educacional para adultos.',
         'assunto': 'Educação'},
        {'id': 61, 'pesquisa': 'Uma startup de tecnologia educacional para adultos pode desenvolver...',
         'assunto': 'Educação'},
        {'id': 62, 'pesquisa': 'Estou pensando em uma startup de aplicativo de gestão financeira pessoal.',
         'assunto': 'Sustentabilidade'},
        {'id': 63, 'pesquisa': 'Uma startup de gestão financeira pessoal pode oferecer um aplicativo que...',
         'assunto': 'Sustentabilidade'},
        {'id': 64, 'pesquisa': 'Preciso de uma ideia para uma startup de soluções de segurança digital.',
         'assunto': 'Tecnologia'},
        {'id': 65, 'pesquisa': 'Uma startup de segurança digital pode inovar ao...', 'assunto': 'Tecnologia'},
        {'id': 66, 'pesquisa': 'Gostaria de uma ideia para uma startup de comércio eletrônico sustentável.',
         'assunto': 'Sustentabilidade'},
        {'id': 67, 'pesquisa': 'Uma startup de comércio eletrônico sustentável pode criar...',
         'assunto': 'Sustentabilidade'},
        {'id': 68, 'pesquisa': 'Quero uma ideia para uma startup de soluções de mobilidade para idosos.',
         'assunto': 'Sustentabilidade'},
        {'id': 69, 'pesquisa': 'Uma startup de mobilidade para idosos pode desenvolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 70, 'pesquisa': 'Estou buscando uma ideia para uma startup de análise de dados para pequenas empresas.',
         'assunto': 'Sustentabilidade'},
        {'id': 71, 'pesquisa': 'Uma startup de análise de dados para pequenas empresas pode...',
         'assunto': 'Sustentabilidade'},
        {'id': 72, 'pesquisa': 'Preciso de uma ideia para uma startup de soluções de gestão de projetos.',
         'assunto': 'Sustentabilidade'},
        {'id': 73, 'pesquisa': 'Uma startup de gestão de projetos pode oferecer...', 'assunto': 'Sustentabilidade'},
        {'id': 74, 'pesquisa': 'Gostaria de uma ideia para uma startup de aplicativo de viagens personalizadas.',
         'assunto': 'Sustentabilidade'},
        {'id': 75, 'pesquisa': 'Uma startup de viagens personalizadas pode criar um aplicativo que...',
         'assunto': 'Sustentabilidade'},
        {'id': 76, 'pesquisa': 'Quero uma ideia para uma startup de soluções de agricultura urbana.',
         'assunto': 'Sustentabilidade'},
        {'id': 77, 'pesquisa': 'Uma startup de agricultura urbana pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 78, 'pesquisa': 'Estou interessado em uma ideia de startup para o setor de vestuário sustentável.',
         'assunto': 'Sustentabilidade'},
        {'id': 79, 'pesquisa': 'Uma startup de vestuário sustentável pode se destacar ao...',
         'assunto': 'Sustentabilidade'},
        {'id': 80, 'pesquisa': 'Preciso de uma ideia para uma startup de marketplace de produtos locais.',
         'assunto': 'Sustentabilidade'},
        {'id': 81, 'pesquisa': 'Uma startup de marketplace de produtos locais pode oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 82, 'pesquisa': 'Gostaria de uma ideia para uma startup de soluções de automação residencial.',
         'assunto': 'Sustentabilidade'},
        {'id': 83, 'pesquisa': 'Uma startup de automação residencial pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 84, 'pesquisa': 'Quero uma ideia para uma startup de soluções de logística reversa.',
         'assunto': 'Sustentabilidade'},
        {'id': 85, 'pesquisa': 'Uma startup de logística reversa pode desenvolver...', 'assunto': 'Sustentabilidade'},
        {'id': 86, 'pesquisa': 'Estou pensando em uma startup de aplicativo de aprendizagem personalizada.',
         'assunto': 'Educação'},
        {'id': 87, 'pesquisa': 'Uma startup de aprendizagem personalizada pode oferecer um aplicativo que...',
         'assunto': 'Educação'},
        {'id': 88, 'pesquisa': 'Preciso de uma ideia para uma startup de soluções de transporte urbano.',
         'assunto': 'Mobilidade Urbana'},
        {'id': 89, 'pesquisa': 'Uma startup de transporte urbano pode se destacar ao...',
         'assunto': 'Mobilidade Urbana'},
        {'id': 90, 'pesquisa': 'Gostaria de uma ideia para uma startup de soluções de gestão de eventos.',
         'assunto': 'Sustentabilidade'},
        {'id': 91, 'pesquisa': 'Uma startup de gestão de eventos pode criar...', 'assunto': 'Sustentabilidade'},
        {'id': 92, 'pesquisa': 'Quero uma ideia para uma startup de tecnologia para facilitar o home office.',
         'assunto': 'Sustentabilidade'},
        {'id': 93, 'pesquisa': 'Uma startup para facilitar o home office pode desenvolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 94, 'pesquisa': 'Estou buscando uma ideia para uma startup de soluções de alimentação saudável.',
         'assunto': 'Sustentabilidade'},
        {'id': 95, 'pesquisa': 'Uma startup de alimentação saudável pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 96, 'pesquisa': 'Preciso de uma ideia para uma startup de soluções de recrutamento inovadoras.',
         'assunto': 'Sustentabilidade'},
        {'id': 97, 'pesquisa': 'Uma startup de recrutamento inovador pode oferecer...', 'assunto': 'Sustentabilidade'},
        {'id': 98, 'pesquisa': 'Gostaria de uma ideia para uma startup de soluções de gerenciamento de tempo.',
         'assunto': 'Sustentabilidade'},
        {'id': 99, 'pesquisa': 'Uma startup de gerenciamento de tempo pode criar...', 'assunto': 'Sustentabilidade'},
        {'id': 100, 'pesquisa': 'Quero uma ideia para uma startup de soluções de comunicação interna.',
         'assunto': 'Sustentabilidade'},
        {'id': 101, 'pesquisa': 'Uma startup de comunicação interna pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 102, 'pesquisa': 'Estou interessado em uma ideia de startup para o setor de energias renováveis.',
         'assunto': 'Energias Renováveis'},
        {'id': 103, 'pesquisa': 'Uma startup de energias renováveis pode se destacar ao...',
         'assunto': 'Energias Renováveis'},
        {'id': 104, 'pesquisa': 'Preciso de uma ideia para uma startup de soluções de gestão de resíduos.',
         'assunto': 'Sustentabilidade'},
        {'id': 105, 'pesquisa': 'Uma startup de gestão de resíduos pode oferecer...', 'assunto': 'Sustentabilidade'},
        {'id': 106, 'pesquisa': 'Gostaria de uma ideia para uma startup de soluções de segurança residencial.',
         'assunto': 'Sustentabilidade'},
        {'id': 107, 'pesquisa': 'Uma startup de segurança residencial pode inovar ao...', 'assunto': 'Sustentabilidade'},
        {'id': 108, 'pesquisa': 'Quero uma ideia para uma startup de soluções de análise de dados para e-commerce.',
         'assunto': 'Sustentabilidade'},
        {'id': 109, 'pesquisa': 'Uma startup de análise de dados para e-commerce pode desenvolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 110, 'pesquisa': 'Estou pensando em uma startup de aplicativo de gestão de tarefas pessoais.',
         'assunto': 'Sustentabilidade'},
        {'id': 111, 'pesquisa': 'Estou pensando em criar uma startup relacionada à educação. Alguma sugestão?',
         'assunto': 'Sustentabilidade'},
        {'id': 112, 'pesquisa': 'Certamente! Uma ideia para uma startup educacional pode ser...', 'assunto': 'Educação'},
        {'id': 113, 'pesquisa': 'Gostaria de algo voltado para o aprendizado de idiomas.',
         'assunto': 'Sustentabilidade'},
        {'id': 114, 'pesquisa': 'Uma startup inovadora de aprendizado de idiomas pode oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 115,
         'pesquisa': 'Isso parece interessante. Como seria uma startup de aprendizado de idiomas usando realidade virtual?',
         'assunto': 'Realidade Virtual'},
        {'id': 116, 'pesquisa': 'Uma startup de aprendizado de idiomas com realidade virtual pode proporcionar...',
         'assunto': 'Realidade Virtual'},
        {'id': 117, 'pesquisa': 'Estou interessado em startups de sustentabilidade. Alguma ideia?',
         'assunto': 'Sustentabilidade'},
        {'id': 118, 'pesquisa': 'Uma startup sustentável pode abordar desafios como...', 'assunto': 'Sustentabilidade'},
        {'id': 119,
         'pesquisa': 'Gostaria de criar uma startup que ajude pequenas empresas a melhorar sua presença online.',
         'assunto': 'Sustentabilidade'},
        {'id': 120, 'pesquisa': 'Uma startup para melhorar a presença online de pequenas empresas pode oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 121, 'pesquisa': 'Pretendo criar uma startup relacionada a alimentos saudáveis. Alguma sugestão única?',
         'assunto': 'Saúde'},
        {'id': 122, 'pesquisa': 'Uma startup de alimentos saudáveis pode se destacar ao oferecer...',
         'assunto': 'Saúde'},
        {'id': 123, 'pesquisa': 'Como seria uma startup que promove a saúde mental no ambiente de trabalho?',
         'assunto': 'Saúde'},
        {'id': 124, 'pesquisa': 'Uma startup de promoção da saúde mental no trabalho pode fornecer...',
         'assunto': 'Saúde'},
        {'id': 125, 'pesquisa': 'Estou interessado em tecnologias limpas. Alguma ideia de startup nesse campo?',
         'assunto': 'Sustentabilidade'},
        {'id': 126, 'pesquisa': 'Uma startup de tecnologias limpas pode focar em soluções como...',
         'assunto': 'Sustentabilidade'},
        {'id': 127, 'pesquisa': 'Como criar uma startup de serviços financeiros inovadores para jovens adultos?',
         'assunto': 'Sustentabilidade'},
        {'id': 128, 'pesquisa': 'Uma startup de serviços financeiros para jovens adultos pode oferecer...',
         'assunto': 'Sustentabilidade'},
        {'id': 129,
         'pesquisa': 'Gostaria de criar uma startup para facilitar o transporte urbano. Alguma ideia disruptiva?',
         'assunto': 'Mobilidade Urbana'},
        {'id': 130, 'pesquisa': 'Uma startup disruptiva para facilitar o transporte urbano pode introduzir...',
         'assunto': 'Mobilidade Urbana'},
        {'id': 131,
         'pesquisa': 'Estou pensando em criar uma startup de entretenimento digital. Alguma sugestão inovadora?',
         'assunto': 'Sustentabilidade'},
        {'id': 132, 'pesquisa': 'Uma startup de entretenimento digital inovadora pode envolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 133, 'pesquisa': 'Como seria uma startup que integra tecnologia e arte de maneira única?',
         'assunto': 'Sustentabilidade'},
        {'id': 134, 'pesquisa': 'Uma startup que integra tecnologia e arte de maneira única pode explorar...',
         'assunto': 'Sustentabilidade'},
        {'id': 135, 'pesquisa': 'Estou interessado em startups de impacto social. Alguma sugestão?',
         'assunto': 'Sustentabilidade'},
        {'id': 136, 'pesquisa': 'Uma startup de impacto social pode abordar questões como...',
         'assunto': 'Sustentabilidade'},
        {'id': 137, 'pesquisa': 'Gostaria de criar uma startup de turismo sustentável. Alguma ideia única?',
         'assunto': 'Sustentabilidade'},
        {'id': 138, 'pesquisa': 'Uma startup de turismo sustentável única pode oferecer experiências como...',
         'assunto': 'Sustentabilidade'},
        {'id': 139,
         'pesquisa': 'Como seria uma startup que utiliza inteligência artificial para resolver problemas ambientais?',
         'assunto': 'Inteligência Artificial'},
        {'id': 140,
         'pesquisa': 'Uma startup que utiliza inteligência artificial para problemas ambientais pode focar em...',
         'assunto': 'Inteligência Artificial'},
        {'id': 141,
         'pesquisa': 'Estou pensando em criar uma startup de tecnologia para idosos. Alguma sugestão inovadora?',
         'assunto': 'Sustentabilidade'},
        {'id': 142, 'pesquisa': 'Uma startup de tecnologia para idosos inovadora pode desenvolver...',
         'assunto': 'Sustentabilidade'},
        {'id': 143, 'pesquisa': 'Como criar uma startup que promove a sustentabilidade no setor da moda?',
         'assunto': 'Sustentabilidade'},
        {'id': 144, 'pesquisa': 'Uma startup de moda sustentável pode introduzir práticas como...',
         'assunto': 'Sustentabilidade'},
        {'id': 145, 'pesquisa': 'Estou interessado em startups de energia renovável. Alguma sugestão?',
         'assunto': 'Energias Renováveis'},
        {'id': 146, 'pesquisa': 'Uma startup de energia renovável pode focar em soluções como...',
         'assunto': 'Energias Renováveis'},
        {'id': 147, 'pesquisa': 'Gostaria de criar uma startup que incentiva o voluntariado. Alguma ideia inspiradora?',
         'assunto': 'Voluntariado'},
        {'id': 148, 'pesquisa': 'Uma startup inspiradora de incentivo ao voluntariado pode envolver...',
         'assunto': 'Voluntariado'},
        {'id': 149, 'pesquisa': 'Como seria uma startup que utiliza blockchain para resolver problemas sociais?',
         'assunto': 'Blockchain'},
        {'id': 150, 'pesquisa': 'Uma startup que utiliza blockchain para resolver problemas sociais pode explorar...',
         'assunto': 'Blockchain'},
        {'id': 151,
         'pesquisa': 'Estou pensando em criar uma startup para simplificar o processo de reciclagem. Alguma sugestão?',
         'assunto': 'Sustentabilidade'},
        {'id': 152, 'pesquisa': 'Uma startup para simplificar a reciclagem pode introduzir métodos como...',
         'assunto': 'Sustentabilidade'},
        {'id': 153,
         'pesquisa': 'Gostaria de criar uma startup que promove a igualdade de gênero. Alguma ideia impactante?',
         'assunto': 'Questões Sociais'},
        {'id': 154,
         'pesquisa': 'Uma startup impactante de promoção da igualdade de gênero pode abordar desafios como...',
         'assunto': 'Questões Sociais'},
        {'id': 155, 'pesquisa': 'Como seria uma startup que utiliza tecnologia para melhorar a qualidade do sono?',
         'assunto': 'Saúde'},
        {'id': 156, 'pesquisa': 'Uma startup que utiliza tecnologia para melhorar o sono pode oferecer...',
         'assunto': 'Saúde'},
        {'id': 157, 'pesquisa': 'Estou interessado em startups de agricultura sustentável. Alguma sugestão única?',
         'assunto': 'Sustentabilidade'},
        {'id': 158, 'pesquisa': 'Uma startup única de agricultura sustentável pode explorar métodos como...?',
         'assunto': 'Sustentabilidade'},
        {'id': 159, 'pesquisa': 'Como criar uma startup de educação financeira para crianças?',
         'assunto': 'Educação Financeira'},
        {'id': 160, 'pesquisa': 'Uma startup de educação financeira para crianças pode envolver...?',
         'assunto': 'Educação Financeira'},
        {'id': 161,
         'pesquisa': 'Gostaria de criar uma startup que promova a saúde mental por meio da música. Alguma ideia criativa?',
         'assunto': 'Saúde'},
        {'id': 162,
         'pesquisa': 'Uma startup criativa para promoção da saúde mental por meio da música pode introduzir...',
         'assunto': 'Saúde'},
        {'id': 163,
         'pesquisa': 'Estou pensando em criar uma startup para conectar profissionais de tecnologia. Alguma sugestão?',
         'assunto': 'Profissionais de tecnologia'},
        {'id': 164, 'pesquisa': 'Uma startup para conectar profissionais de tecnologia pode oferecer...?',
         'assunto': 'Profissionais de tecnologia'},
        {'id': 165,
         'pesquisa': 'Como seria uma startup que utiliza realidade aumentada para melhorar a experiência do cliente no varejo?',
         'assunto': 'Realidade Aumentada'},
        {'id': 166, 'pesquisa': 'Uma startup que utiliza realidade aumentada para o varejo pode proporcionar...?',
         'assunto': 'Realidade Aumentada'},
        {'id': 167,
         'pesquisa': 'Estou interessado em startups que ajudem na transição para energias renováveis. Alguma sugestão inovadora?',
         'assunto': 'Energias Renováveis'},
        {'id': 168,
         'pesquisa': 'Uma startup inovadora para a transição para energias renováveis pode abordar desafios como...?',
         'assunto': 'Energias Renováveis'},
        {'id': 169,
         'pesquisa': 'Gostaria de criar uma startup que utilize inteligência artificial na indústria da moda. Alguma ideia?',
         'assunto': 'Inteligência Artificial'},
        {'id': 170,
         'pesquisa': 'Uma startup que utiliza inteligência artificial na moda pode focar em soluções como...?',
         'assunto': 'Inteligência Artificial'},
        {'id': 171, 'pesquisa': 'Como criar uma startup que incentive hábitos saudáveis por meio de jogos?',
         'assunto': 'Jogos'},
        {'id': 172, 'pesquisa': 'Uma startup que incentiva hábitos saudáveis por meio de jogos pode envolver o que?',
         'assunto': 'Jogos'},
        {'id': 173,
         'pesquisa': 'Estou pensando em criar uma startup para simplificar a gestão de resíduos. Alguma sugestão prática?',
         'assunto': 'Sustentabilidade'},
        {'id': 174, 'pesquisa': 'Uma startup prática para a gestão de resíduos pode introduzir métodos como...?',
         'assunto': 'Sustentabilidade'},
        {'id': 175,
         'pesquisa': 'Gostaria de criar uma startup que conecta doadores a organizações sem fins lucrativos. Alguma ideia?',
         'assunto': 'Saúde'},
        {'id': 176,
         'pesquisa': 'Uma startup que conecta doadores a organizações sem fins lucrativos pode oferecer o que?',
         'assunto': 'Saúde'},
        {'id': 177,
         'pesquisa': 'Como seria uma startup que utiliza aprendizado de máquina para personalizar planos de treino?',
         'assunto': 'Aprendizado de máquina'},
        {'id': 178,
         'pesquisa': 'Uma startup que utiliza aprendizado de máquina para treinos personalizados pode envolver o que?',
         'assunto': 'Aprendizado de máquina'},
        {'id': 179, 'pesquisa': 'Estou interessado em startups de mobilidade urbana. Alguma sugestão inovadora?',
         'assunto': 'Mobilidade Urbana'},
        {'id': 180, 'pesquisa': 'Uma startup inovadora de mobilidade urbana pode abordar desafios como...?',
         'assunto': 'Mobilidade Urbana'},
        {'id': 181,
         'pesquisa': 'Gostaria de criar uma startup para facilitar o aprendizado online. Alguma ideia disruptiva?',
         'assunto': 'Aprendizado Online'},
        {'id': 182, 'pesquisa': 'Uma startup disruptiva para facilitar o aprendizado online pode oferecer o quê?',
         'assunto': 'Aprendizado Online'},
        {'id': 183, 'pesquisa': 'Como criar uma startup que utiliza realidade virtual na área de turismo?',
         'assunto': 'Realidade Virtual'},
        {'id': 184, 'pesquisa': 'Uma startup que utiliza realidade virtual no turismo pode proporcionar o quê?',
         'assunto': 'Realidade Virtual'},
        {'id': 185,
         'pesquisa': 'Estou pensando em criar uma startup de assistência virtual para idosos. Alguma sugestão?',
         'assunto': 'Saúde'},
        {'id': 186, 'pesquisa': 'Uma startup de assistência virtual para idosos pode desenvolver que soluções?',
         'assunto': 'Saúde'},
        {'id': 187,
         'pesquisa': 'Gostaria de criar uma startup que incentive o consumo sustentável. Alguma ideia única?',
         'assunto': 'Sustentabilidade'},
        {'id': 188, 'pesquisa': 'Uma startup única para incentivar o consumo sustentável pode explorar o quê?',
         'assunto': 'Sustentabilidade'},

]


def sugestoes_aleatorio(quantidade):

    return random.sample(sugestoes, quantidade)

def pesquisa_pelo_id(id):

    for item in sugestoes:
        if item['id'] == id:
            return item['pesquisa']
    return None


def todos_assuntos():

    lista = []
    for s in sugestoes:
        if s['assunto'] not in lista:
            lista.append(s['assunto'])

    return lista


def pesquisa_pelo_assunto(assunto):

    lista = []

    for s in sugestoes:
        if s['assunto'] == assunto:
            lista.append(s)

    return lista
