public class UserService {

      public String getUserDisplayName(User user) {
          String name = user.getName();

          if (user == null) {
              return "Anonymous";
          }

          return name;
      }
  }
