# calcula unigramas, bigramas com e sem alisamento
python compute_n_grams.py
# renomeia os bigramas com alisamento para o nome pedido
mv irAlisamento.bigramas irBigramas.txt
mv serAlisamento.bigramas serBigramas.txt
mv lidarAlisamento.bigramas lidarBigramas.txt
mv lerAlisamento.bigramas lerBigramas.txt
# gera ficheiros de resultados
python lema.py ir.unigramas ser.unigramas irBigramas.txt serBigramas.txt foramParametrizacao.txt foramFrases.txt
python lema.py lidar.unigramas ler.unigramas lidarBigramas.txt lerBigramas.txt lidaParametrizacao.txt lidaFrases.txt