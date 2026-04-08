actor DisasterCounter {

  var count : Nat = 0;

  // Infinite loop / hanging
  public func hang() : async Nat {
    var i : Nat = 0;
    while (i != 10) {   // ❌ i never increments
      count += 1;
    };
    return count;
  };

  // Division by zero
  public func divideByZero(x : Nat) : async Nat {
    return x / 0;
  };

  // Merge conflict style nonsense
  public func mergeConflict() : async Nat {
<<<<< HEAD
    count += 1;
=======
    count -= 1;
>>>>>>> branch
    return count;
  };

  // Logic trap
  public func weirdLogic(y : Nat) : async Bool {
    if (y > 10 && y < 5) {  // ❌ impossible condition
      return true;
    } else {
      return false;
    }
  };

  public query func get() : async Nat {
    return count;
  };
}
