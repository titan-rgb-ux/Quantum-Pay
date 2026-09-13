import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../services/transaction_service.dart';
import '../widgets/transaction_card.dart';

class TransactionHistoryScreen extends StatelessWidget {
  final String username;
  const TransactionHistoryScreen({super.key, required this.username});

  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Transaction History')),
    body: FutureBuilder<dynamic>(
      future: TransactionService(ApiService()).history(username),
      builder: (context, snapshot) {
        if (!snapshot.hasData) return const Center(child: CircularProgressIndicator());
        final list = snapshot.data as List;
        return ListView(children: list.map((e) => TransactionCard(tx: Map<String,dynamic>.from(e))).toList());
      },
    ),
  );
}
