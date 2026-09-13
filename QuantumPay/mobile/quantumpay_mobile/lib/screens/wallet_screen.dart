import 'package:flutter/material.dart';
import 'send_money_screen.dart';
import 'transaction_history_screen.dart';

class WalletScreen extends StatelessWidget {
  final String username;
  const WalletScreen({super.key, required this.username});
  @override Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: const Text('Wallet')),
    body: Center(child: Column(mainAxisSize: MainAxisSize.min, children: [
      Text('Welcome $username'),
      ElevatedButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => SendMoneyScreen(username: username))), child: const Text('Send Money')),
      ElevatedButton(onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => TransactionHistoryScreen(username: username))), child: const Text('Transaction History')),
    ])),
  );
}
