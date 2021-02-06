using Microsoft.EntityFrameworkCore;
using System.Linq;

namespace Client.Code.DB
{
    public class Context : DbContext
    {
        public DbSet<Account> Accounts { get; set; }

        public Context(DbContextOptions<Context> options) : base(options)
        {
        }
    }
}
