import 'package:flutter/material.dart';

class RiskBadge extends StatelessWidget {
  final String risk;
  const RiskBadge({super.key, required this.risk});

  @override
  Widget build(BuildContext context) => Chip(label: Text(risk));
}
